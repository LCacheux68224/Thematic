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

from PyQt5.QtCore import QCoreApplication
import os, math
from PyQt5.QtGui import QIcon
from qgis.core import (QgsProcessing,
                       QgsProject,
                       QgsMessageLog,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorLayer,
                       QgsCoordinateReferenceSystem,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFeatureSink,
                       QgsFeatureRequest,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterEnum,
                       QgsFeature)
import processing
# --------------------------- #
# Create a grid from a layer  #
# --------------------------- #

class CreateGridAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT_LAYER = 'OUTPUT_LAYER'
    INPUT = 'INPUT'
    CELL_SIZE = 'CELL_SIZE'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon]
            )
        ) 
        
        self.addParameter(
            QgsProcessingParameterNumber(
                self.CELL_SIZE,
                self.tr('Cell size (in meters)'),
                defaultValue=1000,
                minValue=1,
                optional=False
            )
        )
        
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        '''
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )
        '''
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT_LAYER,
                self.tr("Output layer")
            )
        )
            
    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        
        # INPUT = parameters[self.INPUT]
        # print(self.INPUT.extent())
        # print(INPUT)
        source = self.parameterAsSource(parameters, self.INPUT, context)
        source2 = source.materialize(QgsFeatureRequest())
        crs = source2.crs().authid()


        
        OUTPUT_LAYER = self.parameterAsOutputLayer(parameters,self.OUTPUT_LAYER,context)
        QgsMessageLog.logMessage("output layer : {0}".format(OUTPUT_LAYER), 'Thematic Plugin', 0)
        CELL_SIZE = self.parameterAsInt( parameters, self.CELL_SIZE, context )
        # Layer extent
        layerExtent = source2.extent()
        xmin = (math.floor(layerExtent.xMinimum()/CELL_SIZE)*CELL_SIZE)
        ymin = (math.floor(layerExtent.yMinimum()/CELL_SIZE)*CELL_SIZE)
        xmax = (math.floor(layerExtent.xMaximum()/CELL_SIZE)*CELL_SIZE+CELL_SIZE)
        ymax = (math.floor(layerExtent.yMaximum()/CELL_SIZE)*CELL_SIZE+CELL_SIZE)
        
        # layerExtentList = [xmin,xmax,ymin,ymax]
        layerExtent = "{0},{1},{2},{3}".format(xmin,xmax,ymin,ymax)
        QgsMessageLog.logMessage("Layer extent : {0}".format(layerExtent), 'Thematic Plugin', 0)
        QgsMessageLog.logMessage("Source CRS : {0}".format(dir(crs)), 'Thematic Plugin', 0)
        
        # sourceCrsTexte = str(source.sourceCrs().epsg())
        # print(layerExtent)
        # Creation de la grille
        
        grille = processing.run("qgis:creategrid", 
                        {'TYPE':2,
                         'EXTENT':layerExtent,
                         'HSPACING':CELL_SIZE,
                         'VSPACING':CELL_SIZE,
                         'HOVERLAY':0,
                         'VOVERLAY':0,
                         'CRS':crs,
                         'OUTPUT':'memory:'},
                         feedback=feedback)
        
        # Selection des carreaux utiles
        processing.run("native:selectbylocation", 
                {'INPUT':grille['OUTPUT'],
                 'PREDICATE':[0],
                 'INTERSECT':source2,
                 'METHOD':0},feedback=feedback)
                            
        # On ne garde que les carreaux selectionnes
        result1 = processing.run("native:saveselectedfeatures", 
            {'INPUT':grille['OUTPUT'],
            'OUTPUT':'memory:'})

        # Ajout des colonnes ID, x et y
        result2 = processing.run("qgis:refactorfields", 
                        {'INPUT':result1['OUTPUT'],
                             'FIELDS_MAPPING':[{'expression': 'to_string("left" +500)+\'_\'+to_string("bottom"+500)', 
                                 'length': 25, 
                                 'name': 'ID', 
                                 'precision': 0, 
                                 'type': 10}, 
                             {'expression': 'left+500',
                                 'length': 24, 
                                 'name': 'x', 
                                 'precision': 0, 
                                 'type': 2}, 
                             {'expression': 'bottom+500', 
                                 'length': 24, 
                                 'name': 'y', 
                                 'precision': 0, 
                                 'type': 2}],
                         'OUTPUT':OUTPUT_LAYER},
                         feedback=feedback)
        QgsMessageLog.logMessage("result : {0}".format(result2['OUTPUT']), 'Thematic Plugin', 0)                         
                

        return {self.OUTPUT_LAYER: 'OUTPUT_LAYER'}
        # iface.addVectorLayer("C:/temp/grille.gpkg", "", "ogr")

        # processing.run("qgis:creategrid", {'TYPE':2,'EXTENT':'99217.0,1242426.0,6049646.0,7110480.0 [EPSG:2154]','HSPACING':10000,'VSPACING':10000,'HOVERLAY':0,'VOVERLAY':0,'CRS':'EPSG:2154','OUTPUT':'memory:'})
        
        '''
            source = self.parameterAsSource(parameters, self.INPUT, context)
            (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                    context, source.fields(), source.wkbType(), source.sourceCrs())

            # Compute the number of steps to display within the progress bar and
            # get features from source
            total = 100.0 / source.featureCount() if source.featureCount() else 0
            features = source.getFeatures()

            for current, feature in enumerate(features):
                # Stop the algorithm if cancel button has been clicked
                if feedback.isCanceled():
                    break

                # Add a feature in the sink
                sink.addFeature(feature, QgsFeatureSink.FastInsert)

                # Update the progress bar
                feedback.setProgress(int(current * total))

            # Return the results of the algorithm. In this case our only result is
            # the feature sink which contains the processed features, but some
            # algorithms may return multiple feature sinks, calculated numeric
            # statistics, etc. These should all be included in the returned
            # dictionary, with keys matching the feature corresponding parameter
            # or output names.
            return {self.OUTPUT: dest_id}
        '''

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'creategrid'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Generate a grid from a vector layer')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Smoothing')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'smoothing'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return CreateGridAlgorithm()

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/grid.png')


# ----------------------------- #
# Smooth datas to a grid layer  #
# ----------------------------- #

class SmoothToGridAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(parameters, self.INPUT, context)
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                context, source.fields(), source.wkbType(), source.sourceCrs())

        # Compute the number of steps to display within the progress bar and
        # get features from source
        total = 100.0 / source.featureCount() if source.featureCount() else 0
        features = source.getFeatures()

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            # Add a feature in the sink
            sink.addFeature(feature, QgsFeatureSink.FastInsert)

            # Update the progress bar
            feedback.setProgress(int(current * total))

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {self.OUTPUT: dest_id}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'smoothtogrid'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Smooth datas to a grid layer >>> COMING SOON ...')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Smoothing')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'smoothing'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return SmoothToGridAlgorithm()

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/grid.png')


class CreateInspireGridAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT_LAYER = 'OUTPUT_LAYER'
    INPUT = 'INPUT'
    EXTENT = 'EXTENT'    
    CELL_SIZE = 'CELL_SIZE'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )
        
        self.extentList = [ 'Métropole - ETRS-LAEA - EPSG:3035', 
                            'Guadeloupe et Martinique - UTM 20N - EPSG:2973',
                            'La Réunion - UTM 40S - EPSG:2975', 
                            'Guyane - UTM 22N - EPSG:2972', 
                            'Mayotte - UTM 38S - EPSG:4471', 
                            'Saint-Pierre-et-Miquelon - UTM 21N - EPSG:4467']
        self.addParameter(
            QgsProcessingParameterEnum(
                self.EXTENT,
                self.tr('Extent'),
                options=self.extentList
            )
        )
        
        self.addParameter(
            QgsProcessingParameterNumber(
                self.CELL_SIZE,
                self.tr('Cell size (in meters)'),
                defaultValue=1000,
                minValue=1,
                optional=False
            )
        )
        
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        '''
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )
        '''
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT_LAYER,
                self.tr("Output layer")
            )
        )
            
    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        
        # INPUT = parameters[self.INPUT]
        # print(self.INPUT.extent())
        # print(INPUT)
        source = self.parameterAsSource(parameters, self.INPUT, context)
        source2 = source.materialize(QgsFeatureRequest())
        crs = source2.crs().authid()
        extentZone = str(self.parameterAsString(parameters, self.EXTENT , context))
        
        crsList = {"0": "3035", "1": "2973", "2":"2975", "3":"2972", "4":"4471", "5":"4467", "6":"4467"}
        crsCode = crsList[extentZone]
        # QgsMessageLog.logMessage("crs zone : {0}".format(crsCode), 'Thematic Plugin', 0)
        feedback.pushInfo(self.tr("Zone EPSG:{0}".format(crsCode)))

        # QgsMessageLog.logMessage("CRS : {0}".format(crs), 'Thematic Plugin', 0)
        temp1 = processing.run("native:reprojectlayer", 
                    {'INPUT':source2,
                    'TARGET_CRS':QgsCoordinateReferenceSystem('EPSG:'+crsCode),
                    'OUTPUT':'memory:'},
                     feedback=feedback)
        # QgsMessageLog.logMessage("temporary output layer : {0}".format(temp1), 'Thematic Plugin', 0)

        layerExtent = temp1['OUTPUT'].extent()    
        OUTPUT_LAYER = self.parameterAsOutputLayer(parameters,self.OUTPUT_LAYER,context)
        # QgsMessageLog.logMessage("output layer : {0}".format(OUTPUT_LAYER), 'Thematic Plugin', 0)
        CELL_SIZE = self.parameterAsInt( parameters, self.CELL_SIZE, context )
        # Layer extent
        # layerExtent = source2.extent()
        xmin = (math.floor(layerExtent.xMinimum()/CELL_SIZE)*CELL_SIZE)
        ymin = (math.floor(layerExtent.yMinimum()/CELL_SIZE)*CELL_SIZE)
        xmax = (math.floor(layerExtent.xMaximum()/CELL_SIZE)*CELL_SIZE+CELL_SIZE)
        ymax = (math.floor(layerExtent.yMaximum()/CELL_SIZE)*CELL_SIZE+CELL_SIZE)
        
        # layerExtentList = [xmin,xmax,ymin,ymax]
        layerExtent = "{0},{1},{2},{3}".format(xmin,xmax,ymin,ymax)
        QgsMessageLog.logMessage("Layer extent : {0}".format(layerExtent), 'Thematic Plugin', 0)
        QgsMessageLog.logMessage("CELL_SIZE : {0}".format(CELL_SIZE), 'Thematic Plugin', 0)
        
        # sourceCrsTexte = str(source.sourceCrs().epsg())
        # print(layerExtent)
        # Creation de la grille
        feedback.pushInfo(self.tr("Génération de la grille"))
        grille = processing.run("qgis:creategrid", 
                        {'TYPE':2,
                         'EXTENT':layerExtent,
                         'HSPACING':CELL_SIZE,
                         'VSPACING':CELL_SIZE,
                         'HOVERLAY':0,
                         'VOVERLAY':0,
                         'CRS':'EPSG:'+crsCode,
                         'OUTPUT':'memory:'},
                         feedback=feedback)
        
        # Selection des carreaux utiles
        feedback.pushInfo(self.tr("Suppression des carreaux inutiles"))
        processing.run("native:selectbylocation", 
                {'INPUT':grille['OUTPUT'],
                 'PREDICATE':[0],
                 'INTERSECT':temp1['OUTPUT'],
                 'METHOD':0},feedback=feedback)
                            
        # On ne garde que les carreaux selectionnes
        result1 = processing.run("native:saveselectedfeatures", 
            {'INPUT':grille['OUTPUT'],
            'OUTPUT':'memory:'})
        refactorfieldsExpression = "'CRS" + crsCode + "RES"+ str(CELL_SIZE) + "mN'" + ' + to_string("left") + ' + "'E'" + ' + to_string("bottom")' 
        # QgsMessageLog.logMessage("expression : {0}".format(refactorfieldsExpression), 'Thematic Plugin', 0)
        # Ajout des colonnes ID, x et y
        feedback.pushInfo(self.tr("Ajout des identifiants des carreaux"))
        result2 = processing.run("qgis:refactorfields", 
                        {'INPUT':result1['OUTPUT'],
                             'FIELDS_MAPPING':[{'expression': refactorfieldsExpression, 
                                 'length': 30, 
                                 'name': 'idINSPIRE', 
                                 'precision': 0, 
                                 'type': 10}, 
                             {'expression': 'left',
                                 'length': 24, 
                                 'name': 'x', 
                                 'precision': 0, 
                                 'type': 2}, 
                             {'expression': 'bottom', 
                                 'length': 24, 
                                 'name': 'y', 
                                 'precision': 0, 
                                 'type': 2}],
                         'OUTPUT':OUTPUT_LAYER},
                         feedback=feedback)
        # QgsMessageLog.logMessage("result : {0}".format(result2['OUTPUT']), 'Thematic Plugin', 0)                         
                

        return {self.OUTPUT_LAYER: 'OUTPUT_LAYER'}
        # iface.addVectorLayer("C:/temp/grille.gpkg", "", "ogr")

        # processing.run("qgis:creategrid", {'TYPE':2,'EXTENT':'99217.0,1242426.0,6049646.0,7110480.0 [EPSG:2154]','HSPACING':10000,'VSPACING':10000,'HOVERLAY':0,'VOVERLAY':0,'CRS':'EPSG:2154','OUTPUT':'memory:'})
        
        '''
            source = self.parameterAsSource(parameters, self.INPUT, context)
            (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                    context, source.fields(), source.wkbType(), source.sourceCrs())

            # Compute the number of steps to display within the progress bar and
            # get features from source
            total = 100.0 / source.featureCount() if source.featureCount() else 0
            features = source.getFeatures()

            for current, feature in enumerate(features):
                # Stop the algorithm if cancel button has been clicked
                if feedback.isCanceled():
                    break

                # Add a feature in the sink
                sink.addFeature(feature, QgsFeatureSink.FastInsert)

                # Update the progress bar
                feedback.setProgress(int(current * total))

            # Return the results of the algorithm. In this case our only result is
            # the feature sink which contains the processed features, but some
            # algorithms may return multiple feature sinks, calculated numeric
            # statistics, etc. These should all be included in the returned
            # dictionary, with keys matching the feature corresponding parameter
            # or output names.
            return {self.OUTPUT: dest_id}
        '''

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'createinspiregrid'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Generate an Inspire grid from a vector layer')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Smoothing')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'smoothing'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return CreateInspireGridAlgorithm()

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/grid.png')
		