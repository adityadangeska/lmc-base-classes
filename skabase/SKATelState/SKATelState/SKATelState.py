# -*- coding: utf-8 -*-
#
# This file is part of the SKATelState project
#
#
#

""" SKATelState

A generic base device for Telescope State for SKA.
"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
from SKABaseDevice import SKABaseDevice
# Additional import
# PROTECTED REGION ID(SKATelState.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  SKATelState.additionnal_import

__all__ = ["SKATelState", "main"]


class SKATelState(SKABaseDevice):
    """
    A generic base device for Telescope State for SKA.
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(SKATelState.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  SKATelState.class_variable

    # -----------------
    # Device Properties
    # -----------------

    TelStateConfigFile = device_property(
        dtype='str',
    )







    # ----------
    # Attributes
    # ----------











    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKABaseDevice.init_device(self)
        # PROTECTED REGION ID(SKATelState.init_device) ENABLED START #
        # PROTECTED REGION END #    //  SKATelState.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(SKATelState.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKATelState.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(SKATelState.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKATelState.delete_device

    # ------------------
    # Attributes methods
    # ------------------


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(SKATelState.main) ENABLED START #
    return run((SKATelState,), args=args, **kwargs)
    # PROTECTED REGION END #    //  SKATelState.main

if __name__ == '__main__':
    main()
