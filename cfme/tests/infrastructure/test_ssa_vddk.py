import fauxfactory
import pytest

from cfme import test_requirements
from cfme.infrastructure.provider.virtualcenter import VMwareProvider
from cfme.utils import conf
from cfme.utils.appliance.implementations.ui import navigate_to
from cfme.utils.generators import random_vm_name
from cfme.utils.hosts import setup_host_creds
from cfme.utils.log import logger
from cfme.markers.env_markers.provider import ONE_PER_VERSION

from wrapanapi import VmState

pytestmark = [
    pytest.mark.tier(3),
    test_requirements.smartstate,
    pytest.mark.meta(server_roles="+smartproxy +smartstate"),
    pytest.mark.provider([VMwareProvider], selector=ONE_PER_VERSION),
    pytest.mark.usefixtures('setup_provider')
]

vddk_versions = [
    ('v5_5'),
    ('v6_0'),
    ('v6_5')
]


@pytest.fixture(scope="module")
def ssa_analysis_profile(appliance):
    collected_files = []
    for file in ["/etc/hosts", "/etc/passwd"]:
        collected_files.append({"Name": file, "Collect Contents?": True})

    analysis_profile_name = 'ssa_analysis_{}'.format(fauxfactory.gen_alphanumeric())
    analysis_profile = appliance.collections.analysis_profiles(
        name=analysis_profile_name,
        description=analysis_profile_name,
        profile_type=appliance.collections.analysis_profiles.VM_TYPE,
        categories=["System"],
        files=collected_files
    )
    analysis_profile.create()
    yield
    if analysis_profile.exists:
        analysis_profile.delete()


@pytest.fixture(params=vddk_versions, ids=([item for item in vddk_versions]), scope='module')
def configure_vddk(request, appliance, provider, vm):
    vddk_version = request.param
    vddk_url = conf.cfme_data.get("basic_info").get("vddk_url").get(vddk_version)
    view = navigate_to(vm, 'Details')
    host = view.entities.summary("Relationships").get_text_of("Host")
    setup_host_creds(provider, host)
    appliance.install_vddk(vddk_url=vddk_url)

    @request.addfinalizer
    def _finalize():
        appliance.uninstall_vddk()
        setup_host_creds(provider, host, remove_creds=True)


@pytest.fixture(scope="module")
def vm(request, provider, small_template_modscope, ssa_analysis_profile):
    """ Fixture to provision instance on the provider """
    vm_name = random_vm_name("ssa", max_length=16)
    vm_obj = provider.appliance.collections.infra_vms.instantiate(vm_name,
                                                                  provider,
                                                                  small_template_modscope.name)
    vm_obj.create_on_provider(find_in_cfme=True, allow_skip="default")
    vm_obj.mgmt.ensure_state(VmState.RUNNING)

    @request.addfinalizer
    def _finalize():
        try:
            vm_obj.cleanup_on_provider()
            provider.refresh_provider_relationships()
        except Exception as e:
            logger.exception(e)

    return vm_obj


@pytest.mark.long_running
def test_ssa_vddk(vm, configure_vddk):
    """Check if different version of vddk works with provider

    """
    vm.smartstate_scan(wait_for_task_result=True)
    view = navigate_to(vm, 'Details')
    c_users = view.entities.summary('Security').get_text_of('Users')
    c_groups = view.entities.summary('Security').get_text_of('Groups')
    assert any([c_users != 0, c_groups != 0])
