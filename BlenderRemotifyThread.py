import socket
import struct
import subprocess
import threading
import json

class BlenderRemotifyThread(threading.Thread):
    data = None
    running = False

    def __init__(self):
        threading.Thread.__init__(self)
        self.data = [0] * 7

    def start(self):
        # Start the thread
        print('BlenderRemotify: Starting tread')
        self.running = True
        threading.Thread.start(self)

    def stop(self):
        # Stop the thread
        print('BlenderRemotify: Stopping thread')
        self.running = False

    def run(self):
        # Setup the network socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.bind(('', 3000))

        # Receive new data from the client
        while self.running:
            try:
                recievedData = sock.recvfrom(4096)
                self.data = json.loads(recievedData[0].decode('utf-8'))
            except socket.timeout:
                pass