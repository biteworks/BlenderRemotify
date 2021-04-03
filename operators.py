import bpy
import socket
import threading
from . BlenderRemotifyThread import BlenderRemotifyThread

class BLENDERREMOTIFY_OT_ServerStarter(bpy.types.Operator):
    bl_idname = 'blenderremotify.serverstarter'
    bl_label = 'Start TCP Server'

    thread = None
    timer = None

    def modal(self, context, event):
        scn = bpy.context.scene
        blenderremotifysprops = scn.blenderremotifysprops

        # Stop the thread when ESCAPE is pressed.
        if event.type == 'ESC':
            blenderremotifysprops.serverIsRunning = False
            self.thread.stop()
            context.window_manager.event_timer_remove(self.timer)

            return {'CANCELLED'}

        # Update the object with the received data.
        if event.type == 'TIMER':
            print(self.thread.data)
            #bpy.data.objects['cube'].location = self.thread.data[:2]
            #bpy.data.objects['cube'].rotation_quaternion = self.thread.data[3:]
        
        return {'PASS_THROUGH'}

    def execute(self, context):
        scn = bpy.context.scene
        blenderremotifysprops = scn.blenderremotifysprops
        
        self.thread = BlenderRemotifyThread()
        self.thread.start()
        blenderremotifysprops.serverIsRunning = True

        self.timer = context.window_manager.event_timer_add(0.01, window=context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}