#########################################################################################
# -*- coding: utf-8 -*-
#
# This file is part of the SKATelState project
#
#
#
#########################################################################################
"""Contain the tests for the SKATelState."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
import pytest
from mock import MagicMock

from PyTango import DevState

# PROTECTED REGION ID(SKATelState.test_additional_imports) ENABLED START #
# PROTECTED REGION END #    //  SKATelState.test_additional_imports


# Device test case
@pytest.mark.usefixtures("tango_context", "initialize_device")
# PROTECTED REGION ID(SKATelState.test_SKATelState_decorators) ENABLED START #
# PROTECTED REGION END #    //  SKATelState.test_SKATelState_decorators
class TestSKATelState(object):
    """Test case for packet generation."""

    properties = {
        'TelStateConfigFile': '',
        'SkaLevel': '4',
        'MetricList': 'healthState',
        'GroupDefinitions': '',
        'CentralLoggingTarget': '',
        'ElementLoggingTarget': '',
        'StorageLoggingTarget': 'localhost',
        }

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = SKATelState.numpy = MagicMock()
        # PROTECTED REGION ID(SKATelState.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  SKATelState.test_mocking

    def test_properties(self, tango_context):
        # Test the properties
        # PROTECTED REGION ID(SKATelState.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  SKATelState.test_properties
        pass

    # PROTECTED REGION ID(SKATelState.test_State_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_State_decorators
    def test_State(self, tango_context):
        """Test for State"""
        # PROTECTED REGION ID(SKATelState.test_State) ENABLED START #
        assert tango_context.device.State() == DevState.UNKNOWN
        # PROTECTED REGION END #    //  SKATelState.test_State

    # PROTECTED REGION ID(SKATelState.test_Status_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_Status_decorators
    def test_Status(self, tango_context):
        """Test for Status"""
        # PROTECTED REGION ID(SKATelState.test_Status) ENABLED START #
        assert tango_context.device.Status() == "The device is in UNKNOWN state."
        # PROTECTED REGION END #    //  SKATelState.test_Status

    # PROTECTED REGION ID(SKATelState.test_GetMetrics_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_GetMetrics_decorators
    def test_GetMetrics(self, tango_context):
        """Test for GetMetrics"""
        # PROTECTED REGION ID(SKATelState.test_GetMetrics) ENABLED START #
        assert tango_context.device.GetMetrics() == ""
        # PROTECTED REGION END #    //  SKATelState.test_GetMetrics

    # PROTECTED REGION ID(SKATelState.test_ToJson_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_ToJson_decorators
    def test_ToJson(self, tango_context):
        """Test for ToJson"""
        # PROTECTED REGION ID(SKATelState.test_ToJson) ENABLED START #
        assert tango_context.device.ToJson("") == ""
        # PROTECTED REGION END #    //  SKATelState.test_ToJson

    # PROTECTED REGION ID(SKATelState.test_GetVersionInfo_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_GetVersionInfo_decorators
    def test_GetVersionInfo(self, tango_context):
        """Test for GetVersionInfo"""
        # PROTECTED REGION ID(SKATelState.test_GetVersionInfo) ENABLED START #
        assert tango_context.device.GetVersionInfo() == [""]
        # PROTECTED REGION END #    //  SKATelState.test_GetVersionInfo

    # PROTECTED REGION ID(SKATelState.test_Reset_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_Reset_decorators
    def test_Reset(self, tango_context):
        """Test for Reset"""
        # PROTECTED REGION ID(SKATelState.test_Reset) ENABLED START #
        assert tango_context.device.Reset() == None
        # PROTECTED REGION END #    //  SKATelState.test_Reset


    # PROTECTED REGION ID(SKATelState.test_buildState_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_buildState_decorators
    def test_buildState(self, tango_context):
        """Test for buildState"""
        # PROTECTED REGION ID(SKATelState.test_buildState) ENABLED START #
        assert tango_context.device.buildState == ''
        # PROTECTED REGION END #    //  SKATelState.test_buildState

    # PROTECTED REGION ID(SKATelState.test_versionId_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_versionId_decorators
    def test_versionId(self, tango_context):
        """Test for versionId"""
        # PROTECTED REGION ID(SKATelState.test_versionId) ENABLED START #
        assert tango_context.device.versionId == ''
        # PROTECTED REGION END #    //  SKATelState.test_versionId

    # PROTECTED REGION ID(SKATelState.test_centralLoggingLevel_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_centralLoggingLevel_decorators
    def test_centralLoggingLevel(self, tango_context):
        """Test for centralLoggingLevel"""
        # PROTECTED REGION ID(SKATelState.test_centralLoggingLevel) ENABLED START #
        assert tango_context.device.centralLoggingLevel == 0
        # PROTECTED REGION END #    //  SKATelState.test_centralLoggingLevel

    # PROTECTED REGION ID(SKATelState.test_elementLoggingLevel_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_elementLoggingLevel_decorators
    def test_elementLoggingLevel(self, tango_context):
        """Test for elementLoggingLevel"""
        # PROTECTED REGION ID(SKATelState.test_elementLoggingLevel) ENABLED START #
        assert tango_context.device.elementLoggingLevel == 0
        # PROTECTED REGION END #    //  SKATelState.test_elementLoggingLevel

    # PROTECTED REGION ID(SKATelState.test_storageLoggingLevel_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_storageLoggingLevel_decorators
    def test_storageLoggingLevel(self, tango_context):
        """Test for storageLoggingLevel"""
        # PROTECTED REGION ID(SKATelState.test_storageLoggingLevel) ENABLED START #
        assert tango_context.device.storageLoggingLevel == 0
        # PROTECTED REGION END #    //  SKATelState.test_storageLoggingLevel

    # PROTECTED REGION ID(SKATelState.test_healthState_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_healthState_decorators
    def test_healthState(self, tango_context):
        """Test for healthState"""
        # PROTECTED REGION ID(SKATelState.test_healthState) ENABLED START #
        assert tango_context.device.healthState == 0
        # PROTECTED REGION END #    //  SKATelState.test_healthState

    # PROTECTED REGION ID(SKATelState.test_adminMode_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_adminMode_decorators
    def test_adminMode(self, tango_context):
        """Test for adminMode"""
        # PROTECTED REGION ID(SKATelState.test_adminMode) ENABLED START #
        assert tango_context.device.adminMode == 0
        # PROTECTED REGION END #    //  SKATelState.test_adminMode

    # PROTECTED REGION ID(SKATelState.test_controlMode_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_controlMode_decorators
    def test_controlMode(self, tango_context):
        """Test for controlMode"""
        # PROTECTED REGION ID(SKATelState.test_controlMode) ENABLED START #
        assert tango_context.device.controlMode == 0
        # PROTECTED REGION END #    //  SKATelState.test_controlMode

    # PROTECTED REGION ID(SKATelState.test_simulationMode_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_simulationMode_decorators
    def test_simulationMode(self, tango_context):
        """Test for simulationMode"""
        # PROTECTED REGION ID(SKATelState.test_simulationMode) ENABLED START #
        assert tango_context.device.simulationMode == False
        # PROTECTED REGION END #    //  SKATelState.test_simulationMode

    # PROTECTED REGION ID(SKATelState.test_testMode_decorators) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.test_testMode_decorators
    def test_testMode(self, tango_context):
        """Test for testMode"""
        # PROTECTED REGION ID(SKATelState.test_testMode) ENABLED START #
        assert tango_context.device.testMode == ''
        # PROTECTED REGION END #    //  SKATelState.test_testMode


