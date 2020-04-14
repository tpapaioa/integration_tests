import fauxfactory
import pytest

from cfme.infrastructure.provider.virtualcenter import VMwareProvider
from cfme.utils.log import logger

pytestmark = [
    pytest.mark.provider([VMwareProvider], scope='module'),
    pytest.mark.usefixtures('has_no_providers_modscope', 'setup_provider_modscope')
]


@pytest.fixture(scope="module", params=[0, 1], ids=["A", "B"])
def fix_mod(request):
    yield request.param


@pytest.fixture(scope="module")
def fake_user_modscope(provider):
    fake_user = fauxfactory.gen_string('alphanumeric', 10)
    logger.info(f"fake_user_modscope setup with value {fake_user!r}.")
    yield fake_user
    logger.info(f"fake_user_modscope teardown with value {fake_user!r}.")


def test_1(provider, fix_mod):
    pass


def test_fake_user_1(fake_user_modscope):
    logger.info(f"test_fake_user_1 called with fake_user_modscope {fake_user_modscope!r}.")


def test_fake_user_2(fake_user_modscope):
    logger.info(f"test_fake_user_2 called with fake_user_modscope {fake_user_modscope!r}.")
