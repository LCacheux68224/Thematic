# -*- coding: utf-8 -*-

"""
***************************************************************************
    ThematicUtils.py

***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

import os
import subprocess

from processing.core.ProcessingConfig import ProcessingConfig
from processing.tools.system import isWindows

class ThematicUtils:
 
    @staticmethod
    def RFolder():
        r_folder = ProcessingConfig.getSetting("THEMATIC_R_FOLDER")	
        return r_folder


