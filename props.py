import bpy

class BlenderRemotifyProps(bpy.types.PropertyGroup):
    serverIsRunning: bpy.props.BoolProperty(
        name="serverIsRunning",
        description="Variable to show if server is running",
        default = False
        )