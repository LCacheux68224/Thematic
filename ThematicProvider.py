# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Thematic
                                 A QGIS plugin
 Thematic cartography tools for processing
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2018-07-19
        copyright            : (C) 2018 by Lionel Cacheux
        email                : lionel.cacheux@gmx.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Lionel Cacheux'
__date__ = '2018-07-19'
__copyright__ = '(C) 2018 by Lionel Cacheux'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'
# from .ThematicUtils import ThematicUtils

from processing.core.ProcessingConfig import ProcessingConfig, Setting
import os
from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProcessingProvider
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication

from .SmoothingAlgorithms import CreateBtbGridAlgorithm
from .SmoothingAlgorithms import CreateInspireGridAlgorithm
# from .SmoothingAlgorithms import SmoothToGridAlgorithm
from .SmoothingAlgorithms import DissolveAlgorithm


from .SymbolsAlgorithms import CreateAutomaticSymbolsAlgorithm
from .SymbolsAlgorithms import CreateCustomSymbolsAlgorithm
from .SymbolsAlgorithms import CreateSymbolsLegendAlgorithm
from .SymbolsAlgorithms import FormatProportionalSymbolsLegendAlgorithm

from .FlowsAlgorithms import CreateLinesAlgorithm
from .FlowsAlgorithms import CreateArrowsAlgorithm
from .FlowsAlgorithms import CreateCustomArrowsAlgorithm
from .FlowsAlgorithms import CreateSaphirArrowsAlgorithm
from .FlowsAlgorithms import CreateCustomSaphirArrowsAlgorithm
from .FlowsAlgorithms import CreateArrowsLegendAlgorithm

from .DiscontinuitiesMapAlgorithms import GetInnerBordersAlgorithm
from .DiscontinuitiesMapAlgorithms import RelativeDiscontinuitiesAlgorithm

from .MetroDomAlgorithms import RapprocheDepAlgorithm
from .MetroDomAlgorithms import ZoomParisAlgorithm

class ThematicProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)        
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'thematic_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
                
    #def load(self):
    #   >"""In this method we add settings needed to configure our
    #   >provider.
    #   >"""
    #   >ProcessingConfig.settingIcons[self.name()] = self.icon()
    #   >ProcessingConfig.addSetting(Setting(self.name(), 'THEMATIC_R_FOLDER', 'R Folder', "C:/Program Files/R/R-4.0.2", valuetype=Setting.FOLDER))
    #   >ProcessingConfig.readSettings()
    #   >self.refreshAlgorithms()
    #   >return True

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        # ProcessingConfig.removeSetting('THEMATIC_R_FOLDER')
        pass


    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        # Load algorithms
        
        alglist = [CreateBtbGridAlgorithm(),
                   # SmoothToGridAlgorithm(),
                   CreateInspireGridAlgorithm(),
                   DissolveAlgorithm(),
                   CreateAutomaticSymbolsAlgorithm(),
                   CreateCustomSymbolsAlgorithm(),
                   CreateSymbolsLegendAlgorithm(),
                   FormatProportionalSymbolsLegendAlgorithm(),
                   CreateLinesAlgorithm(),
                   CreateArrowsAlgorithm(),
                   CreateCustomArrowsAlgorithm(),
                   CreateSaphirArrowsAlgorithm(),
                   CreateCustomSaphirArrowsAlgorithm(),
                   CreateArrowsLegendAlgorithm(),
                   GetInnerBordersAlgorithm(),
                   RelativeDiscontinuitiesAlgorithm(),
                   RapprocheDepAlgorithm(),
                   ZoomParisAlgorithm()
                   ]
                       
        for elem in alglist:
            self.addAlgorithm(elem)


                
    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'thematic'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('Thematic - toolbox for thematic maps')

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()
        
    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/icone.png')