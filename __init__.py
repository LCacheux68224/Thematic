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
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Lionel Cacheux'
__date__ = '2018-07-19'
__copyright__ = '(C) 2018 by Lionel Cacheux'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Thematic class from file Thematic.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ThematicPlugin import ThematicPlugin
    return ThematicPlugin()
