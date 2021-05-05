import bpy
import socket
import threading
from . BlenderRemotifyThread import BlenderRemotifyThread

class BLENDERREMOTIFY_OT_ServerStarter(bpy.types.Operator):
    bl_idname = 'blenderremotify.serverstarter'
    bl_label = 'Start TCP Server'

    thread = None
    timer = None
    receivedData = [0, 0, 0, 0, 0, 0, 0]

    def modal(self, context, event):
        scn = bpy.context.scene
        blenderremotifysprops = scn.blenderremotifysprops

        # Stop the thread when ESCAPE is pressed
        if event.type == 'ESC':
            blenderremotifysprops.serverIsRunning = False
            self.thread.stop()
            context.window_manager.event_timer_remove(self.timer)

            return {'CANCELLED'}

        # Update the received data
        if event.type == 'TIMER':
            if self.receivedData != self.thread.data:
                self.receivedData = self.thread.data
                print(self.receivedData)
        
        return {'PASS_THROUGH'}

    def execute(self, context):
        scn = bpy.context.scene
        blenderremotifysprops = scn.blenderremotifysprops
        
        self.thread = BlenderRemotifyThread()
        self.thread.start()

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        blenderremotifysprops.serverIP = ip_address
        blenderremotifysprops.serverIsRunning = True

        self.timer = context.window_manager.event_timer_add(0.01, window=context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

class BLENDERREMOTIFY_OT_AppendRig(bpy.types.Operator):
    bl_idname = 'blenderremotify.appendrig'
    bl_label = 'Create Camera Rig'

    def execute(self, context):
        addonPath = bpy.utils.user_resource('SCRIPTS', "addons") + '/BlenderRemotify'
        path = addonPath + '/BlenderRemotifyRig.blend\\Collection\\'
        object_name = 'BlenderRemotifyRig'
        bpy.ops.wm.append(filename=object_name, directory=path, active_collection=False)
        return {"FINISHED"}