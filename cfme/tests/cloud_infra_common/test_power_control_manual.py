"""Manual tests"""
import pytest

from cfme import test_requirements

pytestmark = [test_requirements.power, pytest.mark.manual]


@pytest.mark.tier(2)
def test_shutdown_guest_scvmm():
    """
    This test performs the Shutdown Guest from the LifeCycle menu which
    invokes the Hyper-V Guest Services Integration command.  This
    gracefully exits the Windows OS rather than just powering off.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/4h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.4
        casecomponent: Infra
        tags: power
        title: test shutdown guest scvmm
        testSteps:
            1. Add provider scvmm
            2. From collections page, select the VM
            3. Click "Shut down guest" On SCVMM powershell
        expectedResults:
            1.
            2.
            3. Use "$vm = Get-VM -name "name_of_vm"; Find-SCJob-objectId $vm.id -recent"
               to verify VM history shows "Shut down virtual machine" instead of "power off"
    """
    pass


@pytest.mark.tier(1)
def test_vm_relationship_datastore_fileshare_scvmm():
    """
    This test case is valid for SCVMM with Host which have Fileshare storage

    Polarion:
        assignee: ghubale
        initialEstimate: 1/4h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.7
        casecomponent: Infra
        tags: power
        title: test vm relationship datastore fileshare scvmm
        setup:
            1. SCVMM provider should have Host which have Fileshare storage
        testSteps:
            1. Add provider scvmm
            2. Provision Vm into fileshare linked to the host
            3. Check VM's relationships - Datastore
        expectedResults:
            1.
            2.
            3. Datastore should be 'fileshare'
    """
    pass


@pytest.mark.tier(2)
def test_suspend_scvmm2016_from_collection():
    """
    Test the a VM can be Suspended, or Saved, from the Collection Page

    Polarion:
        assignee: ghubale
        initialEstimate: 1/8h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.7
        casecomponent: Infra
        tags: power
        title: test suspend scvmm2016 from collection
        testSteps:
            1. Add provider scvmm2016
            2. From collections page, select the VM
            3. Click "suspend" On SCVMM powershell
        expectedResults:
            1.
            2.
            3. Use "$vm = Get-VM -name "name_of_vm"; Find-SCJob-objectId $vm.id -recent"
               to verify VM history shows "suspend" instead of "power off"
    """
    pass


@pytest.mark.tier(2)
def test_restart_guest_scvmm2016():
    """
    This test performs the Restart Guest from the LifeCycle menu which
    invokes the Hyper-V Guest Services Integration command.  This
    gracefully exits and restarts the Windows OS rather than just powering
    off and back on.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/8h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.7
        casecomponent: Infra
        tags: power
        title: test restart guest scvmm2016
        testSteps:
            1. Add provider scvmm2016
            2. Provision VM
            3. From collections page, Select the VM
            4. Click on "Restart Guest" On SCVMM powershell
        expectedResults:
            1.
            2.
            3.
            4. Use "$vm = Get-VM -name "name_of_vm"; Find-SCJob-objectId $vm.id -recent"
               to verify VM history shows "Shut down virtual machine" instead of "power off"
    """
    pass


@pytest.mark.tier(2)
def test_restart_guest_scvmm():
    """
    This test performs the Restart Guest from the LifeCycle menu which
    invokes the Hyper-V Guest Services Integration command.  This
    gracefully exits and restarts the Windows OS rather than just powering
    off and back on.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/4h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.4
        casecomponent: Infra
        tags: power
        title: test restart guest scvmm
        testSteps:
            1. Add provider scvmm
            2. Provision VM
            3. From collections page, Select the VM
            4. Click on "Restart Guest" On SCVMM powershell
        expectedResults:
            1.
            2.
            3.
            4. Use "$vm = Get-VM -name "name_of_vm"; Find-SCJob-objectId $vm.id -recent"
               to verify VM history shows "Shut down virtual machine" instead of "power off"
    """
    pass


@pytest.mark.tier(2)
def test_power_controls_on_archived_vm():
    """
    This test case is to check power operations are not working on archived VM.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/10h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.7
        casecomponent: Cloud
        tags: power
        title: test power controls on archived vm
        testSteps:
            1. Add any Cloud provider
            2. Provision VM
            3. Delete/Retire this VM (we need Archived VM)
            4. Open Archived Vms/or All Vms and find your VM
            5. Select it's Quadicon and/or open it's Details page
        expectedResults:
            1.
            2.
            3.
            4.
            5. Power control options drop-down should be disabled
    """
    pass


@pytest.mark.tier(2)
def test_power_controls_on_vm_in_stack_cloud():
    """
    This test case is to check power controls on vm in stack cloud.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/3h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.6
        casecomponent: Cloud
        tags: power
        title: test power controls on vm in stack cloud
        testSteps:
            1. Provision a VM via Service (Orchestration template - azure/ec2/rhos)
            2. Navigate to cloud-> stacks-> select a stack
            3. Click on the instance in relationship section of stack summary page
            4. Select it's Quadicon and/or open it's Details page
            5. Check power controls operations on that instance
        expectedResults:
            1.
            2.
            3.
            4.
            5. Power operations applicable for this instance should be working as expected
    """
    pass


@pytest.mark.tier(2)
@pytest.mark.manual('manualonly')
def test_power_operations_from_global_region():
    """
    This test case is to check power operations from Global region
    Setup is 2 or more appliances(DB should be configured manually). One
    is Global region, others are Remote. To get this working enable Central Admin.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/2h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.6
        casecomponent: Control
        tags: power
        title:test power operations from global region
        testSteps:
            1. Take two or more appliances
            2. Configure DB manually
            3. Make one appliance as Global region and others are Remote
            4. Add provider to remote region appliance
            5. Provision VM
            6. Perform power operations on VM from global region
        expectedResults:
            1.
            2.
            3.
            4.
            5.
            6. Power operations applicable for this vm should be working as expected
    """
    pass


@pytest.mark.tier(2)
def test_power_options_on_archived_orphaned_vms_all_page():
    """
    This test case is to check Power option drop-down button is disabled on archived and orphaned
    VMs all page.

    Polarion:
        assignee: ghubale
        initialEstimate: 1/2h
        caseimportance: low
        caseposneg: positive
        testtype: functional
        startsin: 5.9
        casecomponent: Control
        tags: power
        testSteps:
            1. Add provider infrastructure provider
            2. Navigate to Archived or orphaned VMs all page
            3. Select any VM and click on power option drop-down
        expectedResults:
            1.
            2.
            3. As we don't perform any power operations on archived or orphaned VMs. So power
               button drop-down should not present there at all.

    Bugzilla:
        1655477
    """
    pass


@pytest.mark.tier(2)
def test_check_compliance_policy_option_on_vm_summery_page():
    """
    Polarion:
        assignee: ghubale
        initialEstimate: 1/12h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.9
        casecomponent: Control
        tags: power
        testSteps:
            1. Go to Compute--> VM Summary screen.
            2. Select VM with compliance policy
            3. Click on Policy and Compliance check is greyed out.
            4. Click on the actually VM to enter next screen, Check compliance is not greyed out
               and is available.
        expectedResults:
            1.
            2.
            3.
            4. Run compliance check button should be available on VM summary screen

    Bugzilla:
        1560107
    """
    pass


@pytest.mark.tier(2)
@pytest.mark.ignore_stream("5.10")
def test_power_states_with_respective_provider():
    """
    Polarion:
        assignee: ghubale
        initialEstimate: 1/12h
        caseimportance: medium
        caseposneg: positive
        testtype: functional
        startsin: 5.11
        casecomponent: Control
        tags: power
        testSteps:
            1. Provision Azure Instance
            2. In Instance detail page, select Resume from Lifecycle menu
        expectedResults:
            1.
            2. Should not have Resume button there or disable button upon provider

    Bugzilla:
        1541447
    """
    pass


@pytest.mark.tier(1)
def test_archived_instance_status():
    """Tests archived instance status

    Polarion:
        assignee: ghubale
        casecomponent: Cloud
        caseimportance: high
        initialEstimate: 1/8h
        tags: power
        testSteps:
            1. Add cloud provider(rhos, ec2 or azure)
            2. Provision instance and retire it
            3. Navigate to cloud > instance > Instance by provider > archived
            4. See any instance power state
        expectedResults:
            1.
            2.
            3. Cloud instances should be present
            4. Power state of cloud instances should be changed to 'archived'

    Bugzilla:
        1701188
    """


@pytest.mark.tier(1)
def test_orphaned_instance_status():
    """Tests orphaned instance status

    Polarion:
        assignee: ghubale
        initialEstimate: 1/10h
        casecomponent: Cloud
        initialEstimate: 1/8h
        tags: power
        testSteps:
            1. Add cloud provider(rhos, ec2 or azure)
            2. Delete provider
            3. Navigate to cloud > instance > Instance by provider > orphaned
            4. See any instance power state
        expectedResults:
            1.
            2.
            3. Cloud instances should be present
            4. Power state of cloud instances should be changed to 'orphaned'

    Bugzilla:
        1701188
    """
