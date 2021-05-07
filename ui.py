import bpy

class BLENDERREMOTIFY_PT_Panel(bpy.types.Panel):
    bl_label = "BlenderRemotify"
    bl_idname = "BLENDERREMOTIFY_PT_BlenderRemotify"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderRemotify"

    def draw(self, context):
        layout = self.layout
        scn = bpy.context.scene
        blenderremotifysprops = scn.blenderremotifysprops

        box = layout.box()
        row = box.row()
        row.label(text="Camera")
        row = box.row()
        row.operator("blenderremotify.appendrig", text="Create camera rig")

        box = layout.box()
        if blenderremotifysprops.serverIsRunning:
            row = box.row()
            row.label(text="Server is running...")
            row = box.row()
            row.label(text="IP: " + blenderremotifysprops.serverIP)
            row = box.row()
            row.label(text="Port: 3000")
        else:
            row = box.row()
            row.label(text="Server is not running.")
        row = box.row()
        row.operator("blenderremotify.serverstarter", text="Start Server")