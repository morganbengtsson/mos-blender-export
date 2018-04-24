import bpy
import json


def write(dir):
    blender_lamps = bpy.data.lamps

    for blender_lamp in blender_lamps:
        print('Exporting: ' + blender_lamp.name)

        node = blender_lamp.node_tree.nodes.get("Emission")
        color_input = node.inputs.get("Color")
        color = color_input.default_value[:3]

        strength_input = node.inputs.get("Strength")
        strength = strength_input.default_value

        spot_size = blender_lamp.spot_size
        spot_blend = blender_lamp.spot_blend

        transform_matrix = blender_lamp.matrix_local
        transform = list()
        for row in transform_matrix.col:
            transform.extend(list(row))

        light = {"color": tuple(color),
                "strength": float(strength),
                "size": float(spot_size),
                "blend": float(spot_blend),
                 "transform": transform}

        json_file = open(dir + '/' + blender_lamp.name + '.light', 'w')
        json.dump(light, json_file)
        json_file.close()
        print("Wrote file: " + blender_lamp.name + ".light")