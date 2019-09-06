import pytest

from cfme.infrastructure.provider.virtualcenter import VMwareProvider
# from cfme.markers.env_markers.provider import providers
# from cfme.utils.providers import ProviderFilter

pytestmark = [
    pytest.mark.provider([VMwareProvider], scope='module'),
]

@pytest.fixture(scope="module", params=[0, 1], ids=["A", "B"])
def fix_mod(request):
    return request.param

def test_1(provider, fix_mod):
    pass
