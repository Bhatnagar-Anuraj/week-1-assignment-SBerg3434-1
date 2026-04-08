"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

cmds.file(new=True, force=True)

#---GroundPlane(River)-----------------------------------------------------#
#Ground (river) Paramters
ground_width = 75
ground_depth = 50
ground_y_position = 0

#Create the ground (river)
ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
#Position the ground (river)
cmds.move(0, ground_y_position, 0, ground)

#Apply the GroundShader (river shader) to the ground (river) - Blue river
ground_shader = cmds.shadingNode("lambert", asShader=True, name="groundMat")
cmds.setAttr(ground_shader + ".color", 0.054, 0.082, 0.191, type="double3")
cmds.select(ground)
cmds.hyperShade(assign=ground_shader)

#---Riverbanks-------------------------------------------------------------#
#Riverbank Parameters
riverbank_width = ground_width / 2.857142857
riverbank_height = 7.5
riverbank_depth = ground_depth
riverbank_01_x = -(ground_width / 3.077)
riverbank_02_x = ground_width / 3.077

#-Riverbank_01-#
#Create Riverbank 01
riverbank_01 = cmds.polyCube(
    name="riverbank_01",
    width = riverbank_width,
    height = riverbank_height,
    depth = riverbank_depth,
)
#Position Riverbank_01
cmds.move(riverbank_01_x, riverbank_height / 2.0, 0, riverbank_01)

#-Riverbank_02-#
#Create Riverbank 02
riverbank_02 = cmds.polyCube(
    name="riverbank_02",
    width = riverbank_width,
    height = riverbank_height,
    depth = riverbank_depth,
)
#Position Riverbank 02
cmds.move(riverbank_02_x, riverbank_height / 2.0, 0, riverbank_02)

#Group the riverbanks together
riverbanks = cmds.group(riverbank_01, riverbank_02, name="riverbanks_grp")

#Apply the riverbank shader to the riverbanks - Green grass
riverbank_shader = cmds.shadingNode("lambert", asShader=True, name="riverbankMat")
cmds.setAttr(riverbank_shader + ".color", 0.085, 0.204, 0.086, type="double3")
cmds.select(riverbanks)
cmds.hyperShade(assign=riverbank_shader)

#---House--------------------------------------------------------------------#
#-Building-#
#Building Parameters
building_width = 10
building_height = 7
building_depth = 10
building_x = -25
building_z = -15

#Create the main body of the house (the building)
building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]

#Position the building
cmds.move(building_x, riverbank_height + building_height / 2.0, building_z, building)

#-Roof-#
#Roof parameters
roof_scale_y = 0.75
roof_height = building_height / 2.3333
roof_rotation_y = 45

#Create the roof
roof = cmds.polyPyramid(
    name="roof_01",
    numberOfSides=4,
    sideLength=building_width,
)
#Adjust the roof's rotation to align with the building
cmds.setAttr("roof_01.rotateY", roof_rotation_y)

#Adjust the roof's height
cmds.setAttr("roof_01.scaleY", roof_scale_y)

#Position the roof on top of the building
cmds.move(building_x, riverbank_height + building_height + roof_height / 1.131, building_z, roof)

#Group the building and roof together 
house = cmds.group(building, roof, name="house_grp")

#Apply the building shader to the building - Light Brown wood
building_shader = cmds.shadingNode("lambert", asShader=True, name="buildingMat")
cmds.setAttr(building_shader + ".color", 0.165, 0.131, 0.086, type="double3")
cmds.select(building)
cmds.hyperShade(assign=building_shader)

#Apply the roof shader to the roof - Dark Brown wood
roof_shader = cmds.shadingNode("lambert", asShader=True, name="roofMat")
cmds.setAttr(roof_shader + ".color", 0.038, 0.032, 0.023, type="double3")
cmds.select(roof)
cmds.hyperShade(assign=roof_shader)

#---Trees-------------------------------------------------------------------------#
#Decide how many trees there are
trees_amount = 2

#-Tree_01-#
#Tree 01 Parameters
tree_trunk_01_radius = 1.5
tree_trunk_01_height = 8
tree_leaves_01_radius = 5
tree_01_x = 26.6
tree_01_z = 16

#Create the trunk for Tree 01
tree_trunk_01 = cmds.polyCylinder(
    name="tree_trunk_01",
    radius=tree_trunk_01_radius,
    height=tree_trunk_01_height,
)

#Raise the trunk of Tree 01 to the ground plane
cmds.move(0, tree_trunk_01_height / 2.0, 0, tree_trunk_01)

#Create leaves for Tree 01
tree_leaves_01 = cmds.polySphere(
    name="tree_leaves_01",
    radius=tree_leaves_01_radius,
)

#Raise the leaves of Tree 01 to the appropriate height
cmds.move(0, tree_trunk_01_height * 1.5 - 0.5, 0, tree_leaves_01)

#Group Tree Trunk 01 and Tree Leaves 01 into Tree 01
cmds.group(tree_trunk_01, tree_leaves_01, name="tree_01_grp")

#Position Tree 01
cmds.move(tree_01_x, riverbank_height, tree_01_z, "tree_01_grp")

#-Tree_02-#
#Tree 02 Parameters
tree_trunk_02_radius = 1.05
tree_trunk_02_height = 7
tree_leaves_02_radius = 4.25
tree_02_x = 19.5
tree_02_z = -13

#Create the trunk for Tree 02
tree_trunk_02 = cmds.polyCylinder(
    name="tree_trunk_02",
    radius=tree_trunk_02_radius,
    height=tree_trunk_02_height,
)

#Raise the trunk of Tree 02 to the ground plane
cmds.move(0, tree_trunk_02_height / 2.0, 0, tree_trunk_02)

#Create leaves for Tree 02
tree_leaves_02 = cmds.polySphere(
    name="tree_leaves_02",
    radius=tree_leaves_02_radius,
)

#Raise the leaves of Tree 02 to the appropriate height
cmds.move(0, tree_trunk_02_height * 1.5 - 0.5, 0, tree_leaves_02)

#Group Tree Trunk 02 and Tree Leaves 02 into Tree 02
cmds.group(tree_trunk_02, tree_leaves_02, name="tree_02_grp")

#Position Tree 02
cmds.move(tree_02_x, riverbank_height, tree_02_z, "tree_02_grp")

#Group all the trees together
all_trees = [f"tree_0{i+1}_grp" for i in range(trees_amount)]
cmds.group(all_trees, name="trees_grp")

#Apply the trunk shader to the tree trunks - Reddish Brown bark
trunk_shader = cmds.shadingNode("lambert", asShader=True, name="trunkMat")
cmds.setAttr(trunk_shader + ".color", 0.4, 0.145, 0.085, type="double3")
for trunk in [tree_trunk_01, tree_trunk_02]:
    cmds.select(trunk)
    cmds.hyperShade(assign=trunk_shader)

#Apply the leaves shader to the tree leaves - Green leaves
leaves_shader = cmds.shadingNode("lambert", asShader=True, name="leavesMat")
cmds.setAttr(leaves_shader + ".color", 0.093, 0.310, 0.093, type="double3")
for leaves in [tree_leaves_01, tree_leaves_02]:
    cmds.select(leaves)
    cmds.hyperShade(assign=leaves_shader)

#---Bridge--------------------------------------------------------------------------------#
#-BridgeBody-#
#Bridge Body Parameters
bridge_body_length = ground_width - riverbank_width * 2
bridge_body_height = 1.5
bridge_body_width = 9
bridge_body_offset_y = 7
bridge_body_y = riverbank_height + bridge_body_offset_y
bridge_z = 3

#Create the body of the bridge
bridge_body = cmds.polyCube(
    name="bridge_body",
    width = bridge_body_length,
    height = bridge_body_height,
    depth = bridge_body_width,
)

#Position the bridge body
cmds.move(0, bridge_body_y, bridge_z, bridge_body)

#-BridgeStairs-#
#Stair Parameters
step_count = bridge_body_offset_y
step_width = bridge_body_width
step_depth = 1.5
step_height = bridge_body_offset_y / step_count
step_rotation = 90.0

#Create the staircase
for i in range(step_count):
    step_name = f"step_{i}"

    current_height = step_height * (i + 1)
    
    #Create one stair
    cmds.polyCube(name=step_name,
                  width=step_width,
                  height=current_height,
                  depth=step_depth)
    
    #Individual stair position parameters
    x_pos = 0
    y_pos = current_height / 2.0    
    z_pos = i * step_depth           
    
    #Position the stair
    cmds.move(x_pos, y_pos, z_pos, step_name)

#Rotate the entire staircase
if step_rotation != 0:
    all_steps = [f"step_{i}" for i in range(step_count)]
    stair_group_01 = cmds.group(all_steps, name="staircase_grp_01")
    
    #Create the second staircase
    cmds.duplicate(stair_group_01)
    
    #Set the correct rotation for each staircase relative to the bridge body
    cmds.rotate(0, step_rotation, 0, stair_group_01, pivot=[0, 0, 0])
    cmds.rotate(0, step_rotation + 180, 0, "staircase_grp_02", pivot=[0, 0, 0])
    
    #Set the correct position for each staircase relative to the bridge body
    cmds.move(-(bridge_body_length / 2.0 + step_depth * step_count - 0.75), riverbank_height, bridge_z, stair_group_01)
    cmds.move(bridge_body_length / 2.0 + step_depth * step_count - 0.75, riverbank_height, bridge_z, "staircase_grp_02")
    
#Group the bridge body and two staircases together
cmds.group(bridge_body, stair_group_01, "staircase_grp_02", name="bridge_grp")

#Apply the bridge shader to the bridge - Deep Brown wood
bridge_shader = cmds.shadingNode("lambert", asShader=True, name="bridgeMat")
cmds.setAttr(bridge_shader + ".color", 0.072, 0.041, 0.024, type="double3")
cmds.select("bridge_grp")
cmds.hyperShade(assign=bridge_shader)

#---Car------------------------------------------------------------------------------------#
#-CarBody-#
#Car Body Parameters
car_width = 4.8
car_body_height = 2.8
car_body_depth = 8
car_body_offset_y = car_body_height / 3.0

#Create the body of the car
cmds.polyCube(
    name="car_body",
    width = car_width,
    height = car_body_height,
    depth = car_body_depth)

#Position the car so it is above the ground plane and at the right height for the wheels
cmds.move(0, car_body_height / 2.0 + car_body_offset_y, 0, "car_body")

#-Wheels-#
#Wheel Parameters
wheel_count = 4
wheel_radius = car_body_offset_y
wheel_width = car_width / 4.0

#Create the four wheels
for i in range(wheel_count):
    #Create one wheel
    cmds.polyCylinder(
        name=f"wheel_0{i+1}",
        radius=wheel_radius,
        height=wheel_width)

#Group all of the wheels together        
all_wheels = [f"wheel_0{i+1}" for i in range(wheel_count)]
wheels_group = cmds.group(all_wheels, name="wheels_grp")

#Rotate all the wheels so they are facing the right way relative to the body of the car
cmds.rotate(0, 0, 90, all_wheels)

#Position each wheel appropriately relative to the body of the car
cmds.move(car_width / 2.65, wheel_radius, car_body_depth / 2.85, "wheel_01")
cmds.move(-(car_width / 2.65), wheel_radius, car_body_depth / 2.85, "wheel_02")
cmds.move(-(car_width / 2.65), wheel_radius, -(car_body_depth / 2.85), "wheel_03")
cmds.move(car_width / 2.65, wheel_radius, -(car_body_depth / 2.85), "wheel_04")

#-Cabin-#
#Cabin Parameters
cabin_height = car_body_height / 1.35
cabin_depth = car_body_depth * 0.75

#Create the cabin
cmds.polyCube(
    name="cabin",
    width=car_width,
    height=cabin_height,
    depth=cabin_depth)

#Position the cabin appropriately relative to the body of the car
cmds.move(0, car_body_height + car_body_offset_y + cabin_height / 2.0, -(car_body_depth / 8), "cabin")

#Group the car body, wheels, and cabin together
car_full = cmds.group("car_body", "wheels_grp", "cabin", name="car_grp")

#Full Car Parameters
car_x = -26.148
car_y = 14.602
car_rotation_y = 134.669

#Position the full car
cmds.move(car_x, riverbank_height, car_y, "car_grp")

#Rotate the full car
cmds.rotate(0, car_rotation_y, 0, "car_grp")

#Apply the car body shader to the full body of the car - Blue Gray metal
car_shader = cmds.shadingNode("lambert", asShader=True, name="car_Mat")
cmds.setAttr(car_shader + ".color", 0.162, 0.170, 0.284, type="double3")
for car in ["car_body", "cabin"]:
    cmds.select(car)
    cmds.hyperShade(assign=car_shader)

#Apply the wheel shader to the wheels - Black rubber
wheel_shader = cmds.shadingNode("lambert", asShader=True, name="wheelMat")
cmds.setAttr(wheel_shader + ".color", 0.010, 0.010, 0.010, type="double3")
cmds.select("wheels_grp")
cmds.hyperShade(assign=wheel_shader)

#---Boat--------------------------------------------------------------------------------------#
#-BoatBody-#
#Boat Body Parameters
boat_side_length = 8
boat_length = 10
boat_offset_y = boat_side_length / 10.416

#Create the body of the boat (a triangular prism)
cmds.polyPrism(
    name="boat_body",
    sideLength=boat_side_length,
    length=boat_length)

#Bevel one edge of the boat body prism so it looks like the body of a boat
cmds.polyBevel("boat_body.e[8]", segments=1, offset=1, offsetAsFraction=True)

#Rotate the body of the boat so it is moving down the river
cmds.rotate(90, 0, 270, "boat_body")

#Scale the body of the boat to a more appropriate proportion
cmds.scale(0.69, 1, 1, "boat_body")

#Move the body of the boat up so it is on the ground (river) plane
cmds.move(0, boat_offset_y, 0, "boat_body")

#-Mast-#
#Mast Parameters
mast_radius = boat_length / 22.2222
mast_height = boat_length

#Create the mast
cmds.polyCylinder(
    name="mast",
    radius = mast_radius,
    height = mast_height)
    
#Position the mast in the right location relative to the body of the boat
cmds.move(0, boat_side_length / 3.5 + mast_height / 2.0, 0, "mast")

#-Sail-#
#Sail Parameters
sail_thickness = mast_radius / 1.2162
sail_height = mast_height / 1.25

#Create the sail
cmds.polyPrism(
    name="sail",
    sideLength=sail_height,
    length=sail_thickness)

#Rotate the sail so it is facing the right way to be a sail (relative to the boat body)
cmds.rotate(90, 0, 0, "sail")

#Position the sail appropriately along the mast and relative to the body of the boat
cmds.move(mast_radius / 0.1957, mast_height / 1.25, 0, "sail")

#Group the boat body, mast, and sail together
boat = cmds.group("boat_body", "mast", "sail", name="boat_grp")

#Full Boat Parameters
boat_x = 0
boat_z = -9

#Position the full boat
cmds.move(boat_x, 0, boat_z, "boat_grp")

#Apply the boat shader to the boat body and sail - White metal/cloth
boat_shader = cmds.shadingNode("lambert", asShader=True, name="boat_Mat")
cmds.setAttr(boat_shader + ".color", 0.540, 0.540, 0.540, type="double3")
for boat in ["boat_body", "sail"]:
    cmds.select(boat)
    cmds.hyperShade(assign=boat_shader)

#Apply the mast shader to the mast - Deep Navy metal
mast_shader = cmds.shadingNode("lambert", asShader=True, name="mastMat")
cmds.setAttr(mast_shader + ".color", 0.010, 0.010, 0.041, type="double3")
cmds.select("mast")
cmds.hyperShade(assign=mast_shader)

#---Frame the scene so all objects are showing---#
cmds.viewFit(allObjects=True)

#Generate feedback for a successful generation
print("Scene built successfully!")




