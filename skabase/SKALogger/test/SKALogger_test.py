#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the SKALogger project
#
#
#
# Distributed under the terms of the none license.
# See LICENSE.txt for more info.
"""Contain the tests for the SKALogger."""

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
from SKALogger import SKALogger

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
class SKALoggerDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(SKALogger.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  SKALogger.test_additionnal_import
    device = SKALogger
    properties = {'SkaLevel': '4', 'MetricList': 'healthState', 'GroupDefinitions': '', 'CentralLoggingTarget': '', 'ElementLoggingTarget': '', 'StorageLoggingTarget': 'localhost', 'CentralLoggingLevelDefault': '2', 'ElementLoggingLevelDefault': '3', 'StorageLoggingLevelDefault': '4', 
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = SKALogger.numpy = MagicMock()
        # PROTECTED REGION ID(SKALogger.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  SKALogger.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(SKALogger.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  SKALogger.test_properties
        pass

    def test_Log(self):
        """Test for Log"""
        # PROTECTED REGION ID(SKALogger.test_Log) ENABLED START #
        assert tango_context.device.Log([""]) == None
        # PROTECTED REGION END #    //  SKALogger.test_Log

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(SKALogger.test_State) ENABLED START #
        assert tango_context.device.State() == DevState.UNKNOWN
        # PROTECTED REGION END #    //  SKALogger.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(SKALogger.test_Status) ENABLED START #
        assert tango_context.device.Status() == "The device is in UNKNOWN state."
        # PROTECTED REGION END #    //  SKALogger.test_Status

    def test_SetCentralLoggingLevel(self):
        """Test for SetCentralLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_SetCentralLoggingLevel) ENABLED START #
        assert tango_context.device.SetCentralLoggingLevel("") == None
        # PROTECTED REGION END #    //  SKALogger.test_SetCentralLoggingLevel

    def test_SetElementLoggingLevel(self):
        """Test for SetElementLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_SetElementLoggingLevel) ENABLED START #
        assert tango_context.device.SetElementLoggingLevel("") == None
        # PROTECTED REGION END #    //  SKALogger.test_SetElementLoggingLevel

    def test_SetStorageLoggingLevel(self):
        """Test for SetStorageLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_SetStorageLoggingLevel) ENABLED START #
        assert tango_context.device.SetStorageLoggingLevel("") == None
        # PROTECTED REGION END #    //  SKALogger.test_SetStorageLoggingLevel

    def test_GetMetrics(self):
        """Test for GetMetrics"""
        # PROTECTED REGION ID(SKALogger.test_GetMetrics) ENABLED START #
        assert tango_context.device.GetMetrics() == ""
        # PROTECTED REGION END #    //  SKALogger.test_GetMetrics

    def test_ToJson(self):
        """Test for ToJson"""
        # PROTECTED REGION ID(SKALogger.test_ToJson) ENABLED START #
        assert tango_context.device.ToJson("") == ""
        # PROTECTED REGION END #    //  SKALogger.test_ToJson

    def test_GetVersionInfo(self):
        """Test for GetVersionInfo"""
        # PROTECTED REGION ID(SKALogger.test_GetVersionInfo) ENABLED START #
        assert tango_context.device.GetVersionInfo() == [""]
        # PROTECTED REGION END #    //  SKALogger.test_GetVersionInfo

    def test_Reset(self):
        """Test for Reset"""
        # PROTECTED REGION ID(SKALogger.test_Reset) ENABLED START #
        assert tango_context.device.Reset() == None
        # PROTECTED REGION END #    //  SKALogger.test_Reset

    def test_buildState(self):
        """Test for buildState"""
        # PROTECTED REGION ID(SKALogger.test_buildState) ENABLED START #
        assert tango_context.device.buildState == ''
        # PROTECTED REGION END #    //  SKALogger.test_buildState

    def test_versionId(self):
        """Test for versionId"""
        # PROTECTED REGION ID(SKALogger.test_versionId) ENABLED START #
        assert tango_context.device.versionId == ''
        # PROTECTED REGION END #    //  SKALogger.test_versionId

    def test_centralLoggingLevel(self):
        """Test for centralLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_centralLoggingLevel) ENABLED START #
        assert tango_context.device.centralLoggingLevel == 0
        # PROTECTED REGION END #    //  SKALogger.test_centralLoggingLevel

    def test_elementLoggingLevel(self):
        """Test for elementLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_elementLoggingLevel) ENABLED START #
        assert tango_context.device.elementLoggingLevel == 0
        # PROTECTED REGION END #    //  SKALogger.test_elementLoggingLevel

    def test_storageLoggingLevel(self):
        """Test for storageLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_storageLoggingLevel) ENABLED START #
        assert tango_context.device.storageLoggingLevel == 0
        # PROTECTED REGION END #    //  SKALogger.test_storageLoggingLevel

    def test_healthState(self):
        """Test for healthState"""
        # PROTECTED REGION ID(SKALogger.test_healthState) ENABLED START #
        assert tango_context.device.healthState == 0
        # PROTECTED REGION END #    //  SKALogger.test_healthState

    def test_adminMode(self):
        """Test for adminMode"""
        # PROTECTED REGION ID(SKALogger.test_adminMode) ENABLED START #
        assert tango_context.device.adminMode == 0
        # PROTECTED REGION END #    //  SKALogger.test_adminMode

    def test_controlMode(self):
        """Test for controlMode"""
        # PROTECTED REGION ID(SKALogger.test_controlMode) ENABLED START #
        assert tango_context.device.controlMode == 0
        # PROTECTED REGION END #    //  SKALogger.test_controlMode

    def test_simulationMode(self):
        """Test for simulationMode"""
        # PROTECTED REGION ID(SKALogger.test_simulationMode) ENABLED START #
        assert tango_context.device.simulationMode == False
        # PROTECTED REGION END #    //  SKALogger.test_simulationMode

    def test_testMode(self):
        """Test for testMode"""
        # PROTECTED REGION ID(SKALogger.test_testMode) ENABLED START #
        assert tango_context.device.testMode == ''
        # PROTECTED REGION END #    //  SKALogger.test_testMode


# Main execution
if __name__ == "__main__":
    main()
