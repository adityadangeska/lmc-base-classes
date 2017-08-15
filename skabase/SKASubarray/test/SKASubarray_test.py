#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the SKASubarray project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.
"""Contain the tests for the SKASubarray."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from time import sleep
from mock import MagicMock
from PyTango import DevFailed, DevState
from devicetest import DeviceTestCase, main
from SKASubarray import SKASubarray

# Note:
#
# Since the device uses an inner thread, it is necessary to
# wait during the tests in order the let the device update itself.
# Hence, the sleep calls have to be secured enough not to produce
# any inconsistent behavior. However, the unittests need to run fast.
# Here, we use a factor 3 between the read period and the sleep calls.
#
# Look at devicetest examples for more advanced testing


# Device test case
class SKASubarrayDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(SKASubarray.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  SKASubarray.test_additionnal_import
    device = SKASubarray
    properties = {'SkaLevel': '4', 'CentralLoggingTarget': '', 'ElementLoggingTarget': '', 'StorageLoggingTarget': 'localhost', 'CentralLoggingLevelDefault': '', 'ElementLoggingLevelDefault': '', 'StorageLoggingLevelStorage': '', 'MetricList': 'healthState,adminMode,controlMode', 'GroupDefinitions': '', 
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = SKASubarray.numpy = MagicMock()
        # PROTECTED REGION ID(SKASubarray.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  SKASubarray.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(SKASubarray.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  SKASubarray.test_properties
        pass

    def test_AssignResources(self):
        """Test for AssignResources"""
        # PROTECTED REGION ID(SKASubarray.test_AssignResources) ENABLED START #
        self.device.AssignResources("")
        # PROTECTED REGION END #    //  SKASubarray.test_AssignResources

    def test_AddResources(self):
        """Test for AddResources"""
        # PROTECTED REGION ID(SKASubarray.test_AddResources) ENABLED START #
        self.device.AddResources("")
        # PROTECTED REGION END #    //  SKASubarray.test_AddResources

    def test_RemoveResources(self):
        """Test for RemoveResources"""
        # PROTECTED REGION ID(SKASubarray.test_RemoveResources) ENABLED START #
        self.device.RemoveResources("")
        # PROTECTED REGION END #    //  SKASubarray.test_RemoveResources

    def test_RemoveAllResources(self):
        """Test for RemoveAllResources"""
        # PROTECTED REGION ID(SKASubarray.test_RemoveAllResources) ENABLED START #
        self.device.RemoveAllResources()
        # PROTECTED REGION END #    //  SKASubarray.test_RemoveAllResources

    def test_ObsState(self):
        """Test for ObsState"""
        # PROTECTED REGION ID(SKASubarray.test_ObsState) ENABLED START #
        self.device.ObsState()
        # PROTECTED REGION END #    //  SKASubarray.test_ObsState

    def test_Reset(self):
        """Test for Reset"""
        # PROTECTED REGION ID(SKASubarray.test_Reset) ENABLED START #
        self.device.Reset()
        # PROTECTED REGION END #    //  SKASubarray.test_Reset

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(SKASubarray.test_State) ENABLED START #
        self.device.State()
        # PROTECTED REGION END #    //  SKASubarray.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(SKASubarray.test_Status) ENABLED START #
        self.device.Status()
        # PROTECTED REGION END #    //  SKASubarray.test_Status

    def test_GetMetrics(self):
        """Test for GetMetrics"""
        # PROTECTED REGION ID(SKASubarray.test_GetMetrics) ENABLED START #
        self.device.GetMetrics()
        # PROTECTED REGION END #    //  SKASubarray.test_GetMetrics

    def test_ToJson(self):
        """Test for ToJson"""
        # PROTECTED REGION ID(SKASubarray.test_ToJson) ENABLED START #
        self.device.ToJson("")
        # PROTECTED REGION END #    //  SKASubarray.test_ToJson

    def test_GetVersionInfo(self):
        """Test for GetVersionInfo"""
        # PROTECTED REGION ID(SKASubarray.test_GetVersionInfo) ENABLED START #
        self.device.GetVersionInfo()
        # PROTECTED REGION END #    //  SKASubarray.test_GetVersionInfo

    def test_subID(self):
        """Test for subID"""
        # PROTECTED REGION ID(SKASubarray.test_subID) ENABLED START #
        self.device.subID
        # PROTECTED REGION END #    //  SKASubarray.test_subID

    def test_resources(self):
        """Test for resources"""
        # PROTECTED REGION ID(SKASubarray.test_resources) ENABLED START #
        self.device.resources
        # PROTECTED REGION END #    //  SKASubarray.test_resources

    def test_obsState(self):
        """Test for obsState"""
        # PROTECTED REGION ID(SKASubarray.test_obsState) ENABLED START #
        self.device.obsState
        # PROTECTED REGION END #    //  SKASubarray.test_obsState

    def test_obsMode(self):
        """Test for obsMode"""
        # PROTECTED REGION ID(SKASubarray.test_obsMode) ENABLED START #
        self.device.obsMode
        # PROTECTED REGION END #    //  SKASubarray.test_obsMode

    def test_configurationProgress(self):
        """Test for configurationProgress"""
        # PROTECTED REGION ID(SKASubarray.test_configurationProgress) ENABLED START #
        self.device.configurationProgress
        # PROTECTED REGION END #    //  SKASubarray.test_configurationProgress

    def test_configurationDelayExpected(self):
        """Test for configurationDelayExpected"""
        # PROTECTED REGION ID(SKASubarray.test_configurationDelayExpected) ENABLED START #
        self.device.configurationDelayExpected
        # PROTECTED REGION END #    //  SKASubarray.test_configurationDelayExpected

    def test_buildState(self):
        """Test for buildState"""
        # PROTECTED REGION ID(SKASubarray.test_buildState) ENABLED START #
        self.device.buildState
        # PROTECTED REGION END #    //  SKASubarray.test_buildState

    def test_versionId(self):
        """Test for versionId"""
        # PROTECTED REGION ID(SKASubarray.test_versionId) ENABLED START #
        self.device.versionId
        # PROTECTED REGION END #    //  SKASubarray.test_versionId

    def test_centralLoggingLevel(self):
        """Test for centralLoggingLevel"""
        # PROTECTED REGION ID(SKASubarray.test_centralLoggingLevel) ENABLED START #
        self.device.centralLoggingLevel
        # PROTECTED REGION END #    //  SKASubarray.test_centralLoggingLevel

    def test_elementLoggingLevel(self):
        """Test for elementLoggingLevel"""
        # PROTECTED REGION ID(SKASubarray.test_elementLoggingLevel) ENABLED START #
        self.device.elementLoggingLevel
        # PROTECTED REGION END #    //  SKASubarray.test_elementLoggingLevel

    def test_storageLoggingLevel(self):
        """Test for storageLoggingLevel"""
        # PROTECTED REGION ID(SKASubarray.test_storageLoggingLevel) ENABLED START #
        self.device.storageLoggingLevel
        # PROTECTED REGION END #    //  SKASubarray.test_storageLoggingLevel

    def test_healthState(self):
        """Test for healthState"""
        # PROTECTED REGION ID(SKASubarray.test_healthState) ENABLED START #
        self.device.healthState
        # PROTECTED REGION END #    //  SKASubarray.test_healthState

    def test_adminMode(self):
        """Test for adminMode"""
        # PROTECTED REGION ID(SKASubarray.test_adminMode) ENABLED START #
        self.device.adminMode
        # PROTECTED REGION END #    //  SKASubarray.test_adminMode

    def test_controlMode(self):
        """Test for controlMode"""
        # PROTECTED REGION ID(SKASubarray.test_controlMode) ENABLED START #
        self.device.controlMode
        # PROTECTED REGION END #    //  SKASubarray.test_controlMode

    def test_simulationMode(self):
        """Test for simulationMode"""
        # PROTECTED REGION ID(SKASubarray.test_simulationMode) ENABLED START #
        self.device.simulationMode
        # PROTECTED REGION END #    //  SKASubarray.test_simulationMode

    def test_testMode(self):
        """Test for testMode"""
        # PROTECTED REGION ID(SKASubarray.test_testMode) ENABLED START #
        self.device.testMode
        # PROTECTED REGION END #    //  SKASubarray.test_testMode

    def test_activationTime(self):
        """Test for activationTime"""
        # PROTECTED REGION ID(SKASubarray.test_activationTime) ENABLED START #
        self.device.activationTime
        # PROTECTED REGION END #    //  SKASubarray.test_activationTime

    def test_maxCapabilities(self):
        """Test for maxCapabilities"""
        # PROTECTED REGION ID(SKASubarray.test_maxCapabilities) ENABLED START #
        self.device.maxCapabilities
        # PROTECTED REGION END #    //  SKASubarray.test_maxCapabilities

    def test_availableCapabilities(self):
        """Test for availableCapabilities"""
        # PROTECTED REGION ID(SKASubarray.test_availableCapabilities) ENABLED START #
        self.device.availableCapabilities
        # PROTECTED REGION END #    //  SKASubarray.test_availableCapabilities


# Main execution
if __name__ == "__main__":
    main()