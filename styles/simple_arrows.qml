<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" minScale="1e+08" version="3.4.12-Madeira" simplifyAlgorithm="0" simplifyLocal="1" simplifyDrawingHints="1" hasScaleBasedVisibilityFlag="0" styleCategories="Symbology|Rendering|CustomProperties|GeometryOptions" simplifyDrawingTol="1">
  <renderer-v2 forceraster="0" enableorderby="0" symbollevels="0" type="singleSymbol">
    <symbols>
      <symbol alpha="1" clip_to_extent="1" force_rhr="0" type="line" name="0">
        <layer pass="0" enabled="1" locked="0" class="ArrowLine">
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
          <prop v="1" k="is_repeated"/>
          <prop v="0" k="offset"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
          <prop v="0" k="ring_filter"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="arrowHeadLength">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="coalesce(scale_linear(abs( &quot;FLUX&quot; ), 0, 8800, 26520.85/10,26520.85), 0)/1.2" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
                <Option type="Map" name="arrowHeadThickness">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="coalesce(scale_linear(abs( &quot;FLUX&quot; ), 0, 8800, 26520.85/10,26520.85), 0)/1.2" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
                <Option type="Map" name="arrowStartWidth">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="coalesce(scale_linear(abs( &quot;FLUX&quot; ), 0, 8800, 0,26520.85), 0)" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
                <Option type="Map" name="arrowWidth">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="coalesce(scale_linear(abs( &quot;FLUX&quot; ), 0, 8800, 0,26520.85), 0)" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
                <Option type="Map" name="offset">
                  <Option value="true" type="bool" name="active"/>
                  <Option value="coalesce(scale_linear(abs( &quot;FLUX&quot; ), 0, 8800, 0,26520.85), 0)/1.5" type="QString" name="expression"/>
                  <Option value="3" type="int" name="type"/>
                </Option>
              </Option>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" clip_to_extent="1" force_rhr="0" type="fill" name="@0@0">
            <layer pass="0" enabled="1" locked="0" class="SimpleFill">
              <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
              <prop v="31,120,180,255" k="color"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="50,50,50,193" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.1" k="outline_width"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="solid" k="style"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" type="QString" name="name"/>
                  <Option name="properties"/>
                  <Option value="collection" type="QString" name="type"/>
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
  <customproperties>
    <property value="&quot;ORIGINE&quot;" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <layerGeometryType>1</layerGeometryType>
</qgis>
