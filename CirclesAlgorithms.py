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
import os
from PyQt5.QtGui import QIcon
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsMessageLog,
                       QgsLogger,
                       QgsFeatureRequest,
                       QgsWkbTypes,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterDefinition,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterField,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterString,
                       QgsProcessingParameterFeatureSink)
import processing 

# defaultMaxValue = 0
# defaultMaxRadius = 0
# ---------------------------- #
# Create proportional circles  #
# ---------------------------- #

class CreateAutomaticSymbolsAlgorithm(QgsProcessingAlgorithm):
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
    ANALYSIS_LAYER = 'ANALYSIS_LAYER'
    COLUMN = 'COLUMN'
    SHAPE = 'SHAPE'
    METHOD = 'METHOD'
    EXTENDED_ANALYSIS = 'EXTENDED ANALYSIS'
    LEGEND = 'LEGEND'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.oldMaxRadius = 0
        self.oldMaxValue = 0
            
        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon,QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )
                        
        self.addParameter(QgsProcessingParameterField(
                self.COLUMN,
                self.tr('Value to represent'),
                None,
                self.INPUT,
                QgsProcessingParameterField.Numeric,
                False
            )
        )
        
        self.shapes = [self.tr('Circles'), self.tr('Diamons'), self.tr('Squares')]
        self.addParameter(QgsProcessingParameterEnum(
                self.SHAPE,
                self.tr('Type of representation'),
                options=self.shapes
            )
        )         

        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.ANALYSIS_LAYER,
                self.tr('Polygon layer used for an automatic scale'),
                [QgsProcessing.TypeVectorPolygon],
                optional=False
            )
        )        

        self.addParameter(
            QgsProcessingParameterBoolean(self.LEGEND,
                self.tr('Add an automatic legend layer'),
                defaultValue=False))
                
            
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
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
        source = self.parameterAsSource(parameters, self.INPUT, context).materialize(QgsFeatureRequest())
        stockValue = self.parameterAsString(parameters, self.COLUMN , context)  
        analysisLayer = self.parameterAsSource(parameters, self.ANALYSIS_LAYER, context)        
        OUTPUT = self.parameterAsOutputLayer(parameters,self.OUTPUT,context)       
        
        """
        sqlQuerry = 'select * from input1 order by {0} DESC'.format(stockValue)
        source = processing.run("qgis:executesql",
                {'INPUT_DATASOURCES':[source0.sourceName()],
                 'INPUT_QUERY':sqlQuerry,
                 'INPUT_UID_FIELD':'',
                 'INPUT_GEOMETRY_FIELD':'',
                 'INPUT_GEOMETRY_TYPE':0,
                 'INPUT_GEOMETRY_CRS':None,
                 'OUTPUT':'memory:'},
                 feedback=feedback)
        # QgsMessageLog.logMessage("extended : {0}".format(dir(source)), 'Thematic Plugin', 0)                  
        """
        '''
        if source.geometryType() == QgsWkbTypes.PolygonGeometry :
            # feedback.pushInfo(self.tr('Transformation en points'))
            source2 = processing.run("native:pointonsurface", 
                                    {'INPUT':source ,
                                     'ALL_PARTS':False,
                                     'OUTPUT':'memory:'},
                                     feedback=feedback)
            source = source2['OUTPUT']
        '''
        # area of the analysis layer for automatic scale
        features = analysisLayer.materialize(QgsFeatureRequest()).getFeatures()
        layerArea = sum([element.geometry().area() for element in features])
            
        selection = processing.run("native:selectbylocation", 
                    {'INPUT': source ,
                     'PREDICATE':[0],
                     'INTERSECT':analysisLayer.materialize(QgsFeatureRequest()),
                     'METHOD':0},
                      feedback = feedback)
                     
        selectedPoints = processing.run("native:saveselectedfeatures", 
                    {'INPUT':source,
                     'OUTPUT':'memory:'})
                     
        features = selectedPoints['OUTPUT'].getFeatures()
        attributeList = sorted([abs(element[stockValue]) for element in features if element[stockValue] != None], reverse=True)
        feedback.pushInfo(self.tr('     AttributeList'.format(attributeList)))
        val1 = attributeList[0]
        if attributeList[1] <= val1 / 3 :
            val2 = attributeList[1]
        else : 
            val2 = val1/3
        if attributeList[2] <= val2 /3:
            val3= attributeList[2]
        else :
            val3 = val2/3

        summary = processing.run("qgis:basicstatisticsforfields", 
                        {'INPUT_LAYER':selectedPoints['OUTPUT'],
                            'FIELD_NAME':stockValue
                        },
                        feedback = feedback)

        radiusFormula = '2*sqrt(abs("{0}")*{1}/(7*pi()*{2}))'.format(stockValue, layerArea, summary['SUM'])
        
        # Check if variable names VAL, R and VARIABLE exist in attribute list - if TRUE then increment
        fieldList = [field.name() for field in source.fields()]    
        
        valueName, radiusName, varName = 'VAL', 'R', 'VAR'
        i , iLabel = 0, ''
        while (valueName+iLabel) in fieldList \
                or (radiusName+iLabel) in fieldList \
                or (varName+iLabel) in fieldList:
            i += 1
            iLabel = '_'+str(i)

        valueName       += iLabel
        radiusName      += iLabel
        varName         += iLabel
        
        # Ajout de la colonne R
        radiusAttribute = processing.run("qgis:fieldcalculator", 
                        {'INPUT':source,
                         'FIELD_NAME':radiusName,
                         'FIELD_TYPE':0,
                         'FIELD_LENGTH':10,
                         'FIELD_PRECISION':3,
                         'NEW_FIELD':True,
                         'FORMULA':radiusFormula,
                         'OUTPUT':'memory:'},
                          feedback=feedback)
        
        # crs = source2.crs().authid()

        # Type of symbols
        represetation = self.parameterAsInt( parameters, self.SHAPE, context )
        if self.parameterAsInt( parameters, self.SHAPE, context ) == 0:
            # circles
            representation = 2
        elif self.parameterAsInt( parameters, self.SHAPE, context ) == 1:
            representation = 1
        else:
            # squares
            representation = 0
            
        centroid = processing.run("native:centroids", 
                        {'INPUT':radiusAttribute['OUTPUT'],
                         'ALL_PARTS':False,
                         'OUTPUT':'memory:'},
                          feedback = feedback)   
        '''                  
        sqlQuerry = 'select * from input1 order by {0} DESC'.format(radiusName)
        source10 = centroid['OUTPUT']
        orderedShape = processing.run("qgis:executesql",
                {'INPUT_DATASOURCES':[source10],
                 'INPUT_QUERY':sqlQuerry,
                 'INPUT_UID_FIELD':'',
                 'INPUT_GEOMETRY_FIELD':'',
                 'INPUT_GEOMETRY_TYPE':0,
                 'INPUT_GEOMETRY_CRS':None,
                 'OUTPUT':'memory:'},
                 feedback = feedback)
        '''                                 
        # QgsMessageLog.logMessage("extended : {0}".format(dir(source)), 'Thematic Plugin', 0)
        
        result = processing.run("qgis:rectanglesovalsdiamondsvariable",
                        {'INPUT': centroid['OUTPUT'],
                         'SHAPE':representation,
                         'WIDTH':radiusName,
                         'HEIGHT':radiusName,
                         'ROTATION':None,
                         'SEGMENTS':36,
                         'OUTPUT':OUTPUT},
                          feedback = feedback)

        feedback.pushInfo('____________________')
        feedback.pushInfo('')
        feedback.pushInfo(self.tr('   Analyse en ronds étendue'))        
        feedback.pushInfo(self.tr("     • Valeur représentée : {0}".format(stockValue)))
        # feedback.pushInfo('Analyse étendue : {0} '.format(extendedAnalysis))
        feedback.pushInfo('')
        feedback.pushInfo(self.tr('   Échelle'))
        feedback.pushInfo(self.tr('     • Val_Max : {0}'.format(val1))) 
        feedback.pushInfo(self.tr('     • R_Max : {0}'.format('????')))        
        feedback.pushInfo('')
        feedback.pushInfo(self.tr('   Valeurs représentées dans l\'échelle'))        
        feedback.pushInfo("     • val1 : {0}".format(val1))
        feedback.pushInfo("     • val2 : {0}".format(val2))
        feedback.pushInfo("     • val3 : {0}".format(val3))        
        feedback.pushInfo('____________________')
        feedback.pushInfo('')  
        
        global defaultMaxValue
        global defaultMaxRadius
        defaultMaxValue = 100
        defaultMaxRadius = 100
        
        return {self.OUTPUT: 'OUTPUT'}
        

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'automaticsymbolsscale'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Symbols with automatic scale')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Proportional symbols')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'proportionalsymbols'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return CreateAutomaticSymbolsAlgorithm()

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/iconRonds.png')
        
    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Description html")    

# ---------------------------- #
# Create custom symbols layer  #
# ---------------------------- #

class CreateCustomSymbolsAlgorithm(QgsProcessingAlgorithm):
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
    COLUMN = 'COLUMN'
    MAX_RADIUS = 'MAX_RADIUS'
    MAX_VALUE = 'MAX_VALUE'
    SHAPE = 'SHAPE'
    METHOD = 'METHOD'
    LEGEND = 'LEGEND'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.oldMaxRadius = 0
        self.oldMaxValue = 0
            
        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorPolygon,QgsProcessing.TypeVectorPoint],
                optional=False
            )
        )

                        
        self.addParameter(QgsProcessingParameterField(
                self.COLUMN,
                self.tr('Value to represent'),
                None,
                self.INPUT,
                QgsProcessingParameterField.Numeric,
                False
            )
        )

        
        self.shapes = [self.tr('Circles'), self.tr('Diamons'), self.tr('Squares')]
        self.addParameter(QgsProcessingParameterEnum(
                self.SHAPE,
                self.tr('Type of representation'),
                options=self.shapes
            )
        ) 
        

        self.addParameter(
            QgsProcessingParameterNumber(
                self.MAX_VALUE,
                self.tr('Max value'),
                minValue=0,
                optional=False
            )
        )
        
        self.addParameter(
            QgsProcessingParameterNumber(
                self.MAX_RADIUS,
                self.tr('Max radius (in meters)'),
                minValue=0,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterBoolean(self.LEGEND,
                self.tr('Add an automatic legend layer'),
                defaultValue=False))
                
            
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
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
        
        source = self.parameterAsSource(parameters, self.INPUT, context).materialize(QgsFeatureRequest())
        stockValue = self.parameterAsString(parameters, self.COLUMN , context)  

        OUTPUT = self.parameterAsOutputLayer(parameters,self.OUTPUT,context)
        
        features = source.getFeatures()
        attributeList = sorted([abs(element[stockValue]) for element in features if element[stockValue] != None], reverse=True)
        val1 = attributeList[0]
        if attributeList[1] <= val1 / 3 :
            val2 = attributeList[1]
        else : 
            val2 = val1/3
        if attributeList[2] <= val2 /3:
            val3= attributeList[2]
        else :
            val3 = val2/3
        
        maxRadius = self.parameterAsInt(parameters,self.MAX_RADIUS,context)
        maxValue = self.parameterAsInt(parameters,self.MAX_VALUE,context)        

        radiusFormula = '{0} * sqrt(abs("{1}")/{2})'.format(maxRadius,stockValue,maxValue)
        feedback.pushInfo(self.tr("formule du rayon : {0}".format(radiusFormula)))            
        fieldList = [field.name() for field in source.fields()]    
        
        valueName, radiusName, varName = 'VAL', 'R', 'VARIABLE'
        i , iLabel = 0, ''
        while (valueName+iLabel) in fieldList \
                or (radiusName+iLabel) in fieldList \
                or (varName+iLabel) in fieldList:
            i += 1
            iLabel = '_'+str(i)
            QgsMessageLog.logMessage("R : {0}".format(iLabel), 'Thematic Plugin', 0)

        valueName       += iLabel
        radiusName      += iLabel
        varName    += iLabel
        
        # Ajout de la colonne R
        radiusAttribute = processing.run("qgis:fieldcalculator", 
                        {'INPUT':source,
                         'FIELD_NAME':radiusName,
                         'FIELD_TYPE':0,
                         'FIELD_LENGTH':10,
                         'FIELD_PRECISION':3,
                         'NEW_FIELD':True,
                         'FORMULA':radiusFormula,
                         'OUTPUT':'memory:'},
                          feedback=feedback)
       
        # Type of symbols
        represetation = self.parameterAsInt( parameters, self.SHAPE, context )
        if self.parameterAsInt( parameters, self.SHAPE, context ) == 0:
            # circles
            representation = 2
        elif self.parameterAsInt( parameters, self.SHAPE, context ) == 1:
            representation = 1
        else:
            # squares
            representation = 0

        centroid = processing.run("native:centroids", 
                        {'INPUT':radiusAttribute['OUTPUT'],
                         'ALL_PARTS':False,
                         'OUTPUT':'memory:'},
                          feedback = feedback)   

        result = processing.run("qgis:rectanglesovalsdiamondsvariable",
                        {'INPUT': centroid['OUTPUT'],
                         'SHAPE':representation,
                         'WIDTH':'R',
                         'HEIGHT':'R',
                         'ROTATION':None,
                         'SEGMENTS':36,
                         'OUTPUT':OUTPUT},
                          feedback = feedback)

        feedback.pushInfo('____________________')
        feedback.pushInfo('')
        feedback.pushInfo(self.tr("     • Valeur représentée : {0}".format(stockValue)))
        # feedback.pushInfo('Analyse étendue : {0} '.format(extendedAnalysis))
        feedback.pushInfo('')
        feedback.pushInfo(self.tr('   Échelle automatique'))
        feedback.pushInfo(self.tr('     • Val_Max : {0}'.format(val1))) 
        feedback.pushInfo(self.tr('     • R_Max : {0}'.format('????')))        
        feedback.pushInfo('')
        feedback.pushInfo(self.tr('   Valeurs représentées dans l\'échelle'))        
        feedback.pushInfo("     • val1 : {0}".format(val1))
        feedback.pushInfo("     • val2 : {0}".format(val2))
        feedback.pushInfo("     • val3 : {0}".format(val3))        
        feedback.pushInfo('____________________')
        feedback.pushInfo('')  
        
        return {self.OUTPUT: 'OUTPUT'}
        

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'customsymbolsscale'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Symbols with custom scale')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Proportional symbols')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'proportionalsymbols'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return CreateCustomSymbolsAlgorithm()

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/iconRonds.png')
        
    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Description html") 

# ---------------------------- #
# Create circles legend #
# ---------------------------- #

class CreateCirclesLegendAlgorithm(QgsProcessingAlgorithm):
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
    COLUMNS = 'COLUMNS'
    MAX_RADIUS = 'MAX_RADIUS'
    MAX_VALUE = 'MAX_VALUE'
    VALUES_LIST = 'VALUES_LIST'
    X_LEGEND = 'X_LEGEND'
    Y_LEGEND = 'Y_LEGEND'
    SHAPE = 'SHAPE'
    
    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        
        self.shapes = [self.tr('Circles'), self.tr('Squares')]
        self.addParameter(QgsProcessingParameterEnum(
                self.SHAPE,
                self.tr('Type of representation'),
                options=self.shapes
            )
        ) 

        
        self.addParameter(
            QgsProcessingParameterNumber(
                self.MAX_VALUE,
                self.tr('Max value'),
                minValue=0,
                optional=False
            )
        )
        
        self.addParameter(
            QgsProcessingParameterNumber(
                self.MAX_RADIUS,
                self.tr('Max radius (in meters)'),
                minValue=0,
                optional=False
            )
        )
        
        self.addParameter(
            QgsProcessingParameterString(
                self.VALUES_LIST,
                self.tr('List of values to represent'),
                optional=True
            )
        )
        
        params = []
        params.append(
            QgsProcessingParameterNumber(
                self.X_LEGEND,
                self.tr('X position of the legend'),
                minValue=0,
                optional=True
            )
        )
        
        params.append(
            QgsProcessingParameterNumber(
                self.Y_LEGEND,
                self.tr('Y position of the legend'),
                minValue=0,
                optional=True
            )
        )
        
        for param in params:
            param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
            self.addParameter(param)
            
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

    def shortHelpString(self):
        return self.tr("Légende pour les analyses en ronds.\n \n \
                       <h3>Échelle des ronds</h3> \n \
                       L'échelle des ronds est défini par une valeur (généralement le maximum) associé au rayon correspondant \n \
                       <h3>Les valeurs à représenter</h4> \n \
                       Par défaut l'extension représente les valeurs MAX, MAX//3 ET MAX//9\n \
                       Il est possible de personnaliser l'échelle en indiquant les valeurs que \
                       l'on souhaite représenter en les saisissant de cette manière :\n \
                       100000;15000;5000 \n\n \
                       Les paramètres avancés permettent de placer la légende en un point (X,Y) de manière précise\n\
                       Par défaut la légende se place au centre de l'écran")

                       
    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'createcircleslegend'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Generate legend for proportional circles >>> COMING SOON !...')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Proportional symbols')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'proportionalsymbols'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return CreateCirclesLegendAlgorithm()

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/images/iconRondsLegende.png')


