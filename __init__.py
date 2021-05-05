bl_info = {
    "name": "BlenderRemotify",
    "description": "A Blender addon to remote control blender with TCP",
    "author": "Tobias Wilhelm (biteworks)",
    "version": (0, 0, 2),
    "blender": (2, 83, 0),
    "location": "3D View > Tools > BlenderRemotify",
    "category": "Generic"
}

import bpy
from . props import *
from . operators import *
from . ui import *

classes = (
    BlenderRemotifyProps,
    BLENDERREMOTIFY_PT_Panel,
    BLENDERREMOTIFY_OT_ServerStarter,
    BLENDERREMOTIFY_OT_AppendRig
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.blenderremotifysprops = bpy.props.PointerProperty(type=BlenderRemotifyProps)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.blenderremotifysprops

if __name__ == "__main__":
    register()