<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" maxScale="0" labelsEnabled="1" simplifyAlgorithm="0" version="3.4.12-Madeira" simplifyLocal="1" minScale="1e+08" simplifyDrawingTol="1" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" simplifyDrawingHints="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol name="0" alpha="1" force_rhr="0" clip_to_extent="1" type="fill">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="240,240,240,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.1"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" locked="0" pass="0" class="GeometryGenerator">
          <prop k="SymbolType" v="Line"/>
          <prop k="geometryModifier" v=" make_line(point_n($geometry,10), make_point(x(point_n($geometry,10))+maximum(R)/1.8,y(point_n($geometry,10))))"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol name="@0@1" alpha="1" force_rhr="0" clip_to_extent="1" type="line">
            <layer enabled="1" locked="0" pass="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="0,0,0,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0.1"/>
              <prop k="line_width_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontUnderline="0" fieldName="' ' ||  format_number(VAL,1)" namedStyle="Normal" fontLetterSpacing="0" fontWordSpacing="0" textColor="0,0,0,255" fontCapitals="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" blendMode="0" isExpression="1" fontSize="10" fontSizeUnit="Point" useSubstitutions="0" fontWeight="50" fontItalic="0" previewBkgrdColor="#ffffff" fontFamily="MS Shell Dlg 2" textOpacity="1" multilineHeight="1" fontStrikeout="0">
        <text-buffer bufferJoinStyle="128" bufferDraw="0" bufferSize="1" bufferNoFill="1" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferOpacity="1"/>
        <background shapeRotationType="0" shapeOffsetY="0" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeSizeY="0" shapeSizeX="0" shapeRadiiY="0" shapeSVGFile="" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeJoinStyle="64" shapeRotation="0" shapeType="0" shapeBorderWidth="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeFillColor="255,255,255,255" shapeOpacity="1" shapeOffsetUnit="MM" shapeBorderColor="128,128,128,255" shapeDraw="0"/>
        <shadow shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowOffsetDist="1" shadowDraw="0" shadowUnder="0" shadowOffsetGlobal="1" shadowOpacity="0.7" shadowScale="100" shadowColor="0,0,0,255"/>
        <substitutions/>
      </text-style>
      <text-format multilineAlign="0" autoWrapLength="0" rightDirectionSymbol=">" placeDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0" wrapChar="" formatNumbers="0" decimals="3" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" addDirectionSymbol="0"/>
      <placement labelOffsetMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="1" repeatDistanceUnits="MM" maxCurvedCharAngleIn="25" repeatDistance="0" yOffset="0" dist="0" maxCurvedCharAngleOut="-25" placement="1" quadOffset="5" offsetUnits="MM" rotationAngle="0" priority="5" centroidInside="0" distMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" placementFlags="10" preserveRotation="1" fitInPolygonOnly="0" offsetType="0" distUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR"/>
      <rendering drawLabels="1" obstacleType="0" maxNumLabels="2000" minFeatureSize="0" scaleMax="0" displayAll="1" obstacle="1" mergeLines="0" fontMaxPixelSize="10000" labelPerPart="0" fontMinPixelSize="3" obstacleFactor="1" scaleVisibility="0" limitNumLabels="0" scaleMin="0" upsidedownLabels="0" zIndex="0" fontLimitPixelSize="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties" type="Map">
            <Option name="PositionX" type="Map">
              <Option name="active" value="true" type="bool"/>
              <Option name="expression" value="x( $geometry ) +  maximum( R)/1.8" type="QString"/>
              <Option name="type" value="3" type="int"/>
            </Option>
            <Option name="PositionY" type="Map">
              <Option name="active" value="true" type="bool"/>
              <Option name="expression" value="y(point_n($geometry,10))" type="QString"/>
              <Option name="type" value="3" type="int"/>
            </Option>
          </Option>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory opacity="1" scaleBasedVisibility="0" penWidth="0" lineSizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" width="15" barWidth="5" rotationOffset="270" height="15" scaleDependency="Area" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" enabled="0" minScaleDenominator="0" labelPlacementMethod="XHeight" backgroundAlpha="255" penColor="#000000" minimumSize="0" maxScaleDenominator="1e+08" diagramOrientation="Up" sizeType="MM">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" priority="0" obstacle="0" showAll="1" placement="1" zIndex="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="VAL">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="R">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SECT">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="VAL" index="0"/>
    <alias name="" field="R" index="1"/>
    <alias name="" field="SECT" index="2"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="VAL" applyOnUpdate="0"/>
    <default expression="" field="R" applyOnUpdate="0"/>
    <default expression="" field="SECT" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" field="VAL" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="R" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="SECT" constraints="0" exp_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="VAL" exp="" desc=""/>
    <constraint field="R" exp="" desc=""/>
    <constraint field="SECT" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column name="VAL" width="-1" type="field" hidden="0"/>
      <column name="R" width="-1" type="field" hidden="0"/>
      <column name="SECT" width="-1" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="R" editable="1"/>
    <field name="SECT" editable="1"/>
    <field name="VAL" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="R" labelOnTop="0"/>
    <field name="SECT" labelOnTop="0"/>
    <field name="VAL" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>VAL</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
