<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyDrawingTol="1" labelsEnabled="1" simplifyAlgorithm="0" simplifyDrawingHints="1" simplifyMaxScale="1" simplifyLocal="1" version="3.4.12-Madeira" maxScale="0" minScale="1e+08" readOnly="0" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" forceraster="0" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol type="line" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer class="ArrowLine" enabled="1" pass="0" locked="0">
          <prop v="1" k="arrow_start_width"/>
          <prop v="MapUnit" k="arrow_start_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_start_width_unit_scale"/>
          <prop v="0" k="arrow_type"/>
          <prop v="1" k="arrow_width"/>
          <prop v="MapUnit" k="arrow_width_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="arrow_width_unit_scale"/>
          <prop v="1.5" k="head_length"/>
          <prop v="MapUnit" k="head_length_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_length_unit_scale"/>
          <prop v="1.5" k="head_thickness"/>
          <prop v="MapUnit" k="head_thickness_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="head_thickness_unit_scale"/>
          <prop v="0" k="head_type"/>
          <prop v="1" k="is_curved"/>
          <prop v="0" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if($length/2 &lt; maximum(&quot;WIDTH&quot;), $length/2, maximum(&quot;WIDTH&quot;))"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="0.5*&quot;WIDTH&quot;+.1*maximum(&quot;WIDTH&quot;)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="arrowHeadType">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="case when FLUX >0 then 'single' else 'reversed' end"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="&quot;WIDTH&quot;"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="&quot;WIDTH&quot;"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="offset">
                  <Option type="bool" name="active" value="false"/>
                  <Option type="QString" name="expression" value="0.5*&quot;WIDTH&quot;+.1*maximum(&quot;WIDTH&quot;)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="fill" name="@0@0" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer class="SimpleFill" enabled="1" pass="0" locked="0">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="31,120,180,255" k="color"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.1" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="no" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="fillColor">
                      <Option type="bool" name="active" value="true"/>
                      <Option type="QString" name="expression" value="case when FLUX >0 then @value else 'darkred' end"/>
                      <Option type="int" name="type" value="3"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
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
      <text-style textOpacity="1" fontItalic="0" fieldName="format_number(val,0)" fontSizeUnit="Point" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" multilineHeight="1" fontWeight="50" fontCapitals="0" fontFamily="Arial" isExpression="1" fontWordSpacing="0" blendMode="0" fontSize="8" previewBkgrdColor="#ffffff" namedStyle="Normal" fontStrikeout="0" textColor="0,0,0,255" useSubstitutions="0">
        <text-buffer bufferNoFill="1" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferBlendMode="0" bufferJoinStyle="128" bufferDraw="0" bufferSize="1"/>
        <background shapeFillColor="255,255,255,255" shapeBorderWidthUnit="MM" shapeOffsetUnit="MM" shapeRotationType="0" shapeJoinStyle="64" shapeSVGFile="" shapeRadiiUnit="MM" shapeRadiiX="0" shapeOpacity="1" shapeDraw="0" shapeOffsetY="0" shapeBorderWidth="0" shapeBlendMode="0" shapeRadiiY="0" shapeSizeY="0" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeType="0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeSizeUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0"/>
        <shadow shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOffsetGlobal="1" shadowBlendMode="6" shadowOffsetDist="1" shadowScale="100" shadowRadius="1.5" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
        <substitutions/>
      </text-style>
      <text-format multilineAlign="4294967295" rightDirectionSymbol=">" placeDirectionSymbol="0" formatNumbers="0" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" addDirectionSymbol="0" decimals="3" wrapChar="" autoWrapLength="0" plussign="0" useMaxLineLengthForAutoWrap="1"/>
      <placement maxCurvedCharAngleIn="25" rotationAngle="0" repeatDistance="0" offsetUnits="MM" yOffset="0" placement="4" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" priority="5" xOffset="0" dist="0" quadOffset="4" distUnits="MM" fitInPolygonOnly="0" centroidInside="0" distMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" placementFlags="10" preserveRotation="1" offsetType="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" centroidWhole="0"/>
      <rendering maxNumLabels="2000" obstacleType="0" upsidedownLabels="0" scaleVisibility="0" scaleMin="0" fontMinPixelSize="3" obstacle="1" scaleMax="0" fontMaxPixelSize="10000" limitNumLabels="0" fontLimitPixelSize="0" obstacleFactor="1" zIndex="0" displayAll="1" minFeatureSize="0" labelPerPart="0" mergeLines="0" drawLabels="1"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" name="name" value=""/>
          <Option type="Map" name="properties">
            <Option type="Map" name="PositionX">
              <Option type="bool" name="active" value="true"/>
              <Option type="QString" name="expression" value="x(   end_point( $geometry)  )"/>
              <Option type="int" name="type" value="3"/>
            </Option>
            <Option type="Map" name="PositionY">
              <Option type="bool" name="active" value="true"/>
              <Option type="QString" name="expression" value="y(   end_point( $geometry)  )"/>
              <Option type="int" name="type" value="3"/>
            </Option>
          </Option>
          <Option type="QString" name="type" value="collection"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="&quot;ORIGINE&quot;" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory labelPlacementMethod="XHeight" penColor="#000000" barWidth="5" penWidth="0" penAlpha="255" enabled="0" diagramOrientation="Up" scaleDependency="Area" backgroundColor="#ffffff" height="15" backgroundAlpha="255" lineSizeType="MM" sizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="0" minScaleDenominator="0" opacity="1" sizeScale="3x:0,0,0,0,0,0" rotationOffset="270" minimumSize="0" width="15" maxScaleDenominator="1e+08">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="2" priority="0" obstacle="0" linePlacementFlags="18" zIndex="0" dist="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
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
    <field name="WIDTH">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="VAL" index="0"/>
    <alias name="" field="WIDTH" index="1"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="VAL"/>
    <default expression="" applyOnUpdate="0" field="WIDTH"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" constraints="0" field="VAL" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" constraints="0" field="WIDTH" exp_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="VAL" exp=""/>
    <constraint desc="" field="WIDTH" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="WIDTH" hidden="0" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
      <column type="field" name="VAL" hidden="0" width="-1"/>
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
    <field name="DEST" editable="1"/>
    <field name="DIST_KM" editable="1"/>
    <field name="FLUX" editable="1"/>
    <field name="ORIGINE" editable="1"/>
    <field name="VAL" editable="1"/>
    <field name="WIDTH" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="DEST" labelOnTop="0"/>
    <field name="DIST_KM" labelOnTop="0"/>
    <field name="FLUX" labelOnTop="0"/>
    <field name="ORIGINE" labelOnTop="0"/>
    <field name="VAL" labelOnTop="0"/>
    <field name="WIDTH" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>WIDTH</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
