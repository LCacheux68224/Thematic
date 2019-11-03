<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.4.12-Madeira" simplifyDrawingTol="1" simplifyMaxScale="1" maxScale="0" simplifyAlgorithm="0" simplifyDrawingHints="1" styleCategories="Symbology|Labeling|Rendering|CustomProperties|GeometryOptions" labelsEnabled="1" simplifyLocal="1">
  <renderer-v2 forceraster="0" type="singleSymbol" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol force_rhr="0" name="0" clip_to_extent="1" alpha="1" type="fill">
        <layer enabled="1" locked="0" class="SimpleFill" pass="0">
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
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" locked="0" class="GeometryGenerator" pass="0">
          <prop k="SymbolType" v="Line"/>
          <prop k="geometryModifier" v=" make_line(point_n($geometry,3), make_point(x(point_n($geometry,3))+maximum(WIDTH)/8,y(point_n($geometry,3))))"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" name="@0@1" clip_to_extent="1" alpha="1" type="line">
            <layer enabled="1" locked="0" class="SimpleLine" pass="0">
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
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
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
      <text-style isExpression="1" textOpacity="1" textColor="0,0,0,255" fontStrikeout="0" fieldName="' ' ||  format_number(VAL,1)" fontFamily="MS Shell Dlg 2" fontCapitals="0" fontWeight="50" useSubstitutions="0" fontItalic="0" namedStyle="Normal" fontLetterSpacing="0" multilineHeight="1" previewBkgrdColor="#ffffff" fontSize="10" fontWordSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" blendMode="0" fontUnderline="0" fontSizeUnit="Point">
        <text-buffer bufferJoinStyle="128" bufferDraw="0" bufferColor="255,255,255,255" bufferBlendMode="0" bufferSizeUnits="MM" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferSize="1" bufferNoFill="1"/>
        <background shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeOpacity="1" shapeDraw="0" shapeOffsetY="0" shapeSVGFile="" shapeSizeX="0" shapeBorderWidthUnit="MM" shapeBorderWidth="0" shapeFillColor="255,255,255,255" shapeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeSizeType="0" shapeSizeY="0" shapeOffsetUnit="MM" shapeRadiiX="0" shapeRadiiUnit="MM" shapeBorderColor="128,128,128,255" shapeBlendMode="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotation="0" shapeRotationType="0" shapeSizeUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0"/>
        <shadow shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowDraw="0" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOffsetDist="1" shadowOffsetAngle="135" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowBlendMode="6" shadowUnder="0" shadowRadius="1.5" shadowColor="0,0,0,255" shadowOffsetUnit="MM"/>
        <substitutions/>
      </text-style>
      <text-format wrapChar="" useMaxLineLengthForAutoWrap="1" plussign="0" rightDirectionSymbol=">" multilineAlign="0" formatNumbers="0" addDirectionSymbol="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" decimals="3" autoWrapLength="0" reverseDirectionSymbol="0"/>
      <placement placementFlags="10" offsetUnits="MM" placement="1" dist="0" centroidWhole="1" distMapUnitScale="3x:0,0,0,0,0,0" centroidInside="0" maxCurvedCharAngleIn="25" xOffset="0" quadOffset="5" offsetType="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" distUnits="MM" fitInPolygonOnly="0" maxCurvedCharAngleOut="-25" priority="5" repeatDistance="0" yOffset="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1"/>
      <rendering displayAll="1" obstacleType="0" labelPerPart="0" minFeatureSize="0" obstacleFactor="1" scaleMin="0" drawLabels="1" fontLimitPixelSize="0" obstacle="1" fontMaxPixelSize="10000" limitNumLabels="0" fontMinPixelSize="3" maxNumLabels="2000" mergeLines="0" scaleVisibility="0" upsidedownLabels="0" scaleMax="0" zIndex="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties" type="Map">
            <Option name="PositionX" type="Map">
              <Option value="true" name="active" type="bool"/>
              <Option value="x( point_n($geometry,3) ) +  maximum(WIDTH)/8" name="expression" type="QString"/>
              <Option value="3" name="type" type="int"/>
            </Option>
            <Option name="PositionY" type="Map">
              <Option value="true" name="active" type="bool"/>
              <Option value="y(point_n($geometry,3))" name="expression" type="QString"/>
              <Option value="3" name="type" type="int"/>
            </Option>
          </Option>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <layerGeometryType>2</layerGeometryType>
</qgis>
