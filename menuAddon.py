###########################################################
#
#     This addon made by Shihab.
#
#     This addon completly free.
#      
###########################################################
bl_info = {
     "name"       : "Add Menu", 
     "category"   : "Game Engine", 
     "author"     : "Shihab", 
     "blender"    : (2,79,0), 
     "location"   : "View3D > UI toolbar (n)", 
     "description": "Adds Menu", "version":(2,2), 
     "wiki_url"   : "https://blenderartists.org/t/addon-add-menu/1255135",
    "tracker_url" : "https://blenderartists.org/t/addon-add-menu/1255135"
}

import bpy
import math
import mathutils

def AddMenu():
    scene = bpy.context.scene
    
    #camera menu
    bpy.ops.object.camera_add()
    caM = bpy.context.object
    caM.name = 'Camera_Menu'
    caM.location = ((3, 4, 13))
    caM.rotation_euler = (0, 0, 7.84)
    caM.data.lens = (20)
    bpy.context.scene.camera = caM
    
    #add play and settings
    bpy.ops.mesh.primitive_plane_add()
    play = bpy.context.object
    play.name = 'Play_Button'
    play.game.physics_type = 'STATIC'
    play.scale = ((1.2, 3.2, 1))
    play.location = ((0, 4, 0.3))
    mat = bpy.data.materials.new(name="MAT")
    mat.diffuse_color = (0.288, 0.5, 0.1)
    bpy.ops.object.material_slot_add()
    play.data.materials[0] = mat
    mat.use_shadeless = True

    #text play
    bpy.ops.object.text_add()
    Text = bpy.context.object
    Text.name = 'Text_Play'
    Text.game.physics_type = 'NO_COLLISION'
    Text.scale = ((2, 2, 1))
    Text.location = ((0.6, 1.5, 0.4))
    Text.rotation_euler = (0, 0, 7.84)
    Text.data.body = 'PLAY'
    
    #add developer and settings
    bpy.ops.mesh.primitive_plane_add()
    developer = bpy.context.object
    developer.name = 'Developer_Button'
    developer.game.physics_type = 'STATIC'
    developer.scale = ((1.2, 6.2, 1))
    developer.location = ((3, 4, 0.3))
    bpy.ops.object.material_slot_add()
    developer.data.materials[0] = mat
    
    #text develpoer
    bpy.ops.object.text_add()
    Text3 = bpy.context.object
    Text3.name = 'Text_Developer'
    Text3.game.physics_type = 'NO_COLLISION'
    Text3.scale = ((2, 2, 1))
    Text3.location = ((3.6, -1.9, 0.4))
    Text3.rotation_euler = (0, 0, 7.84)
    Text3.data.body = 'DEVELOPER'
    print('GG')
        
    #add quit and settings
    bpy.ops.mesh.primitive_plane_add()
    Quit = bpy.context.object
    Quit.name = 'Quit_Button'
    Quit.game.physics_type = 'STATIC'
    Quit.scale = ((1.2, 3.2, 1))
    Quit.location = ((6, 4, 0.3))
    bpy.ops.object.material_slot_add()
    Quit.data.materials[0] = mat

    #text quit
    bpy.ops.object.text_add()
    Text2 = bpy.context.object
    Text2.name = 'Text_quit'
    Text2.game.physics_type = 'NO_COLLISION'
    Text2.scale = ((2, 2, 1))
    Text2.location = ((6.6, 1.5, 0.4))
    Text2.rotation_euler = (0, 0, 7.84)
    Text2.data.body = 'QUIT'
    
    #camera menu
    bpy.ops.object.camera_add()
    caM2 = bpy.context.object
    caM2.name = 'Camera_developer'
    caM2.location = ((3, 28, 13))
    caM2.rotation_euler = (0, 0, 7.84)
    caM2.data.lens = (20)
    
    #plane developer
    bpy.ops.mesh.primitive_plane_add()
    imgv = bpy.context.object
    imgv.name = 'Developer Imgae'
    imgv.game.physics_type = "NO_COLLISION"
    imgv.scale = ((6.3, 10.6, 0))
    imgv.location = ((3, 28, 0))
    imgv.rotation_euler = (0, 0, 0)
    mat2 = bpy.data.materials.new(name="MAT Developer")
    bpy.ops.object.material_slot_add()
    imgv.data.materials[0] = mat2
    mat2.use_shadeless = True
    cTx = bpy.data.textures.new("Texture Developer INFO", type = 'IMAGE')
    mtx = mat2.texture_slots.add()
    mtx.texture = cTx
    
    #back plane
    bpy.ops.mesh.primitive_plane_add()
    bak = bpy.context.object
    bak.name = "Back_Button"
    bak.game.physics_type = "STATIC"
    bak.scale = ((1.2, 3.2, 1))
    bak.location = ((7.5, 21.5, 0.2))
    bak.rotation_euler = (0, 0, 0)
    mat3 = bpy.data.materials.new(name="MAT Back Button")
    mat3.diffuse_color = (0.288, 0.5, 0.1)
    bpy.ops.object.material_slot_add()
    bak.data.materials[0] = mat3
    mat3.use_shadeless = True
    #cTex = bpy.data.textures.new("Texture Back", type = 'IMAGE')
    #mtex = mat3.texture_slots.add()
    #mtex.texture = cTex
    #cTex.use_alpha = True
    #mat3.use_transparency = True
    #mat3.alpha = 0.0
    
    #back text
    bpy.ops.object.text_add()
    Text4 = bpy.context.object
    Text4.name = 'Text back'
    Text4.game.physics_type = 'NO_COLLISION'
    Text4.scale = ((2, 2, 1))
    Text4.location = ((8.1, 18.6, 0.3))
    Text4.rotation_euler = (0, 0, 7.84)
    Text4.data.body = 'BACK'
    
    #logic editor for play
    bpy.ops.logic.sensor_add(type="MOUSE",name='left',object=play.name)
    bpy.ops.logic.controller_add(type="LOGIC_AND",object=play.name)
    bpy.ops.logic.actuator_add(type="SCENE",name='playScene',object=play.name)
    play.game.actuators['playScene'].mode = 'SET'
    bpy.ops.logic.sensor_add(type="MOUSE",name='over',object=play.name)
    play.game.sensors['over'].mouse_event = 'MOUSEOVER'
    bpy.ops.logic.sensor_add(type="ALWAYS",name='Always',object=play.name)
    bpy.ops.logic.controller_add(type="LOGIC_AND",object=play.name)
    bpy.ops.logic.actuator_add(type="MOUSE",name='Mouse Show',object=play.name)
    play.game.sensors['Always'].use_tap = True
    play.game.sensors['left'].use_tap = True

    #logic editor for quit
    bpy.ops.logic.sensor_add(type="MOUSE",name='left',object=Quit.name)
    bpy.ops.logic.controller_add(type="LOGIC_AND",object=Quit.name)
    bpy.ops.logic.actuator_add(type="GAME",name='Quit Game',object=Quit.name)
    Quit.game.actuators['Quit Game'].mode = 'QUIT'
    bpy.ops.logic.sensor_add(type="MOUSE",name='over',object=Quit.name)
    Quit.game.sensors['over'].mouse_event = 'MOUSEOVER'
    Quit.game.sensors['left'].use_tap = True
    
    #logic editor for developer
    bpy.ops.logic.sensor_add(type="MOUSE",name='left',object=developer.name)
    bpy.ops.logic.sensor_add(type="MOUSE",name='over',object=developer.name)
    developer.game.sensors['over'].mouse_event = 'MOUSEOVER'
    developer.game.sensors['left'].use_tap = True
    bpy.ops.logic.controller_add(type="LOGIC_AND",object=developer.name)
    bpy.ops.logic.actuator_add(type="SCENE",name='Go_Camera',object=developer.name)
    developer.game.actuators['Go_Camera'].mode = 'CAMERA'
    developer.game.actuators['Go_Camera'].camera = bpy.data.objects["Camera_developer"]
    
    #logic editor for back_button
    bpy.ops.logic.sensor_add(type="MOUSE",name='Left',object=bak.name)
    bpy.ops.logic.sensor_add(type="MOUSE",name='over',object=bak.name)
    bak.game.sensors['over'].mouse_event = 'MOUSEOVER'
    bak.game.sensors['Left'].use_tap = True
    bpy.ops.logic.controller_add(type="LOGIC_AND",object=bak.name)
    bpy.ops.logic.actuator_add(type="SCENE",name='Select Camera Menu',object=bak.name)
    bak.game.actuators['Select Camera Menu'].mode = 'CAMERA'
    bak.game.actuators['Select Camera Menu'].camera = bpy.data.objects["Camera_Menu"]
    
    #link controlles play
    play.game.sensors['left'].link(play.game.controllers[-1])
    play.game.actuators["playScene"].link(play.game.controllers[-1])
    play.game.sensors['over'].link(play.game.controllers[-1])
    play.game.actuators["Mouse Show"].link(play.game.controllers[0])
    play.game.sensors['Always'].link(play.game.controllers[0])
    #link controllers Quit
    Quit.game.sensors['left'].link(Quit.game.controllers[-1])
    Quit.game.actuators["Quit Game"].link(Quit.game.controllers[-1])
    Quit.game.sensors['over'].link(Quit.game.controllers[-1])
    #link conrollers developer
    developer.game.sensors['left'].link(developer.game.controllers[-1])
    developer.game.sensors['over'].link(developer.game.controllers[-1])
    developer.game.actuators["Go_Camera"].link(developer.game.controllers[-1])
    #link controllers bak_button
    bak.game.sensors['Left'].link(bak.game.controllers[-1])
    bak.game.sensors['over'].link(bak.game.controllers[-1])
    bak.game.actuators["Select Camera Menu"].link(bak.game.controllers[-1])
        
class add_menu(bpy.types.Operator):
    bl_idname = "object.add_menu"
    bl_description = 'add a menu (set the scene to play it from menu)'
    bl_label = "Add Menu"
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        AddMenu()
        self.report({'INFO'}, "Menu added")
        return {"FINISHED"}
    
class panel(bpy.types.Panel):
    bl_label = "Menu"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    
    def draw(self,context):
        layout = self.layout
        scene = context.scene
        
        row = layout.row()
        row.scale_y = 1.6
        row.operator("object.add_menu",text='Add Menu')
        
def register():
    bpy.utils.register_class(panel)
    bpy.utils.register_class(add_menu)

def unregister():
    bpy.utils.unregister_class(panel)
    bpy.utils.unregister_class(add_menu)
    
if __name__ == "__main__":
    register()
