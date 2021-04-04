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

        if blenderremotifysprops.serverIsRunning:
            layout.label(text="Server is running...")
            layout.label(text="IP: " + blenderremotifysprops.serverIP)
            layout.label(text="Port: 3000")
        else:
            layout.label(text="Server is not running.")

        layout.operator("blenderremotify.serverstarter", text="Start Server")