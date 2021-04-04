import bpy

class BlenderRemotifyProps(bpy.types.PropertyGroup):
    serverIsRunning: bpy.props.BoolProperty(
        name="serverIsRunning",
        description="Variable to show if server is running",
        default = False
        )
    serverIP: bpy.props.StringProperty(
        name="serverIP",
        description="IP of current host",
        default="127.0.0.1",
        maxlen=1024,
        )