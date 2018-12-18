#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the SKALogger project
#
#
#

"""Contain the tests for the SKALogger."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from mock import MagicMock
from PyTango import DevState, DeviceProxy
import re
import pytest
import logging
import calendar
import time
#from testfixtures import LogCapture
logging.basicConfig()
from logging.handlers import SysLogHandler

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
@pytest.mark.usefixtures("tango_context", "initialize_device")
class TestSKALogger(object):
    """Test case for packet generation."""
    # PROTECTED REGION ID(SKALogger.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  SKALogger.test_additionnal_import
    #device = SKALogger
    properties = {'SkaLevel': '1', 'MetricList': 'healthState', 'GroupDefinitions': '', 'CentralLoggingTarget': '', 'ElementLoggingTarget': '', 'StorageLoggingTarget': 'localhost', 'CentralLoggingLevelDefault': '2', 'ElementLoggingLevelDefault': '3', 'StorageLoggingLevelDefault': '4',
                  }
    #empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = SKALogger.numpy = MagicMock()
        # PROTECTED REGION ID(SKALogger.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  SKALogger.test_mocking

    def test_properties(self, tango_context):
        # test the properties
        # PROTECTED REGION ID(SKALogger.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  SKALogger.test_properties
        pass

    def test_Log(self, tango_context):
        """Test for Log"""
        # PROTECTED REGION ID(SKALogger.test_Log) ENABLED START #
        assert tango_context.device.Log([""]) == None
        # PROTECTED REGION END #    //  SKALogger.test_Log

    def test_State(self, tango_context):
        """Test for State"""
        # PROTECTED REGION ID(SKALogger.test_State) ENABLED START #
        assert tango_context.device.State() == DevState.UNKNOWN
        # PROTECTED REGION END #    //  SKALogger.test_State

    def test_Status(self, tango_context):
        """Test for Status"""
        # PROTECTED REGION ID(SKALogger.test_Status) ENABLED START #
        assert tango_context.device.Status() == "The device is in UNKNOWN state."
        # PROTECTED REGION END #    //  SKALogger.test_Status

    @pytest.mark.parametrize("logging_level", [4])
    @pytest.mark.parametrize("logging_target", ["logger/test/1"])
    def test_SetCentralLoggingLevel(self, tango_context, logging_level, logging_target):
        """Test for SetCentralLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_SetCentralLoggingLevel) ENABLED START #
        levels = []
        levels.append(logging_level)
        targets = []
        targets.append(logging_target)
        device1 = []
        device1.append(levels)
        device1.append(targets)
        tango_context.device.SetCentralLoggingLevel(device1)
        dev1 = DeviceProxy(logging_target)
        assert dev1.centralLoggingLevel == 4
        # PROTECTED REGION END #    //  SKALogger.test_SetCentralLoggingLevel

    @pytest.mark.parametrize("logging_level", [2])
    @pytest.mark.parametrize("logging_target", ["logger/test/1"])
    def test_SetElementLoggingLevel(self, tango_context, logging_level, logging_target):
        """Test for SetElementLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_SetElementLoggingLevel) ENABLED START #
        levels = []
        levels.append(logging_level)
        targets = []
        targets.append(logging_target)
        device1 = []
        device1.append(levels)
        device1.append(targets)
        tango_context.device.SetElementLoggingLevel(device1)
        dev1 = DeviceProxy(logging_target)
        assert dev1.elementLoggingLevel == 2
        # PROTECTED REGION END #    //  SKALogger.test_SetElementLoggingLevel

    @pytest.mark.parametrize("logging_level", [3])
    @pytest.mark.parametrize("logging_target", ["logger/test/1"])
    def test_SetStorageLoggingLevel(self, tango_context, logging_level, logging_target):
        """Test for SetStorageLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_SetStorageLoggingLevel) ENABLED START #
        levels = []
        levels.append(logging_level)
        targets = []
        targets.append(logging_target)
        device1 = []
        device1.append(levels)
        device1.append(targets)
        tango_context.device.SetStorageLoggingLevel(device1)
        dev1 = DeviceProxy(logging_target)
        assert dev1.storageLoggingLevel == 3
        # PROTECTED REGION END #    //  SKALogger.test_SetStorageLoggingLevel

    def test_GetVersionInfo(self, tango_context):
        """Test for GetVersionInfo"""
        # PROTECTED REGION ID(SKALogger.test_GetVersionInfo) ENABLED START #
        # assert tango_context.device.GetVersionInfo() == ["SKALogger, tangods-skabasedevice, 1.0.0, A generic base device for SKA."]
        versionPattern = re.compile(
            r'SKALogger, tangods-skabasedevice, [0-9].[0-9].[0-9], A generic base device for SKA')
        versionInfo = tango_context.device.GetVersionInfo()
        assert (re.match(versionPattern, versionInfo[0])) != None
        # PROTECTED REGION END #    //  SKALogger.test_GetVersionInfo

    def test_Reset(self, tango_context):
        """Test for Reset"""
        # PROTECTED REGION ID(SKALogger.test_Reset) ENABLED START #
        assert tango_context.device.Reset() == None
        # PROTECTED REGION END #    //  SKALogger.test_Reset

    def test_buildState(self, tango_context):
        """Test for buildState"""
        # PROTECTED REGION ID(SKALogger.test_buildState) ENABLED START #
        assert tango_context.device.buildState == 'tangods-skabasedevice, 1.0.0, A generic base device for SKA.'
        # PROTECTED REGION END #    //  SKALogger.test_buildState

    def test_versionId(self, tango_context):
        """Test for versionId"""
        # PROTECTED REGION ID(SKALogger.test_versionId) ENABLED START #
        assert tango_context.device.versionId == '1.0.0'
        # PROTECTED REGION END #    //  SKALogger.test_versionId

    def test_centralLoggingLevel(self, tango_context):
        """Test for centralLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_centralLoggingLevel) ENABLED START #
        assert tango_context.device.centralLoggingLevel == 5
        # PROTECTED REGION END #    //  SKALogger.test_centralLoggingLevel

    def test_elementLoggingLevel(self, tango_context):
        """Test for elementLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_elementLoggingLevel) ENABLED START #
        assert tango_context.device.elementLoggingLevel == 5
        # PROTECTED REGION END #    //  SKALogger.test_elementLoggingLevel

    def test_storageLoggingLevel(self, tango_context):
        """Test for storageLoggingLevel"""
        # PROTECTED REGION ID(SKALogger.test_storageLoggingLevel) ENABLED START #
        assert tango_context.device.storageLoggingLevel == 5
        # PROTECTED REGION END #    //  SKALogger.test_storageLoggingLevel

    def test_healthState(self, tango_context):
        """Test for healthState"""
        # PROTECTED REGION ID(SKALogger.test_healthState) ENABLED START #
        assert tango_context.device.healthState == 0
        # PROTECTED REGION END #    //  SKALogger.test_healthState

    def test_adminMode(self, tango_context):
        """Test for adminMode"""
        # PROTECTED REGION ID(SKALogger.test_adminMode) ENABLED START #
        assert tango_context.device.adminMode == 0
        # PROTECTED REGION END #    //  SKALogger.test_adminMode

    def test_controlMode(self, tango_context):
        """Test for controlMode"""
        # PROTECTED REGION ID(SKALogger.test_controlMode) ENABLED START #
        assert tango_context.device.controlMode == 0
        # PROTECTED REGION END #    //  SKALogger.test_controlMode

    def test_simulationMode(self, tango_context):
        """Test for simulationMode"""
        # PROTECTED REGION ID(SKALogger.test_simulationMode) ENABLED START #
        assert tango_context.device.simulationMode == False
        # PROTECTED REGION END #    //  SKALogger.test_simulationMode

    def test_testMode(self, tango_context):
        """Test for testMode"""
        # PROTECTED REGION ID(SKALogger.test_testMode) ENABLED START #
        assert tango_context.device.testMode == ''
        # PROTECTED REGION END #    //  SKALogger.test_testMode


# # Main execution
# if __name__ == "__main__":
#     main()
