import attr
import pytest

from cfme.fixtures import terminalreporter
from cfme.test_framework.appliance import appliances_from_cli
from cfme.utils.appliance import PodAppliance

PLUGIN_KEY = "pod-appliance"
APP_TYPE = PodAppliance.type


@pytest.hookimpl
def pytest_configure(config):
    app_type = config.getoption('--app-type')
    if APP_TYPE == app_type:
        reporter = terminalreporter.reporter()
        plugin = PodAppliancePlugin()
        config.pluginmanager.register(plugin, PLUGIN_KEY)

        config.option.sprout_template_type = 'openshift_pod'
        config.option.sprout_template_preconfigured = False

        from cfme.test_framework.sprout.plugin import mangle_in_sprout_appliances
        sprout_appliances = mangle_in_sprout_appliances(config)

        appliances = appliances_from_cli(sprout_appliances, None)
        holder = config.pluginmanager.getplugin('appliance-holder')
        reporter.write_line('Retrieved following regular appliances:', cyan=True)
        for appliance in appliances:
            reporter.write_line('* {!r}'.format(appliance), cyan=True)

        holder.stack.push(appliances[0])
        holder.held_appliance = appliances[0]
        holder.pool = appliances


@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    app_type = config.getoption('--app-type')
    if APP_TYPE == app_type:
        holder = config.pluginmanager.getplugin('appliance-holder')
        holder.stack.pop()


@attr.s(eq=False)
class PodAppliancePlugin(object):
    pass
