import bpy
import socket
import struct
import subprocess
import threading

class BlenderRemotifyThread(threading.Thread):
    data = None
    running = False

    def __init__(self):
        threading.Thread.__init__(self)
        self.data = [0] * 7

    def start(self):
        # Start the thread.
        print('Starting TCP tread')
        self.running = True
        threading.Thread.start(self)

    def stop(self):
        # Stop the thread.
        print('Stopping TCP thread')
        self.running = False

    def run(self):
        # Setup the network socket.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.bind(('127.0.0.1', 3000))
        sock.listen(1)

        # Receive new data from the client.
        while self.running:
            try:
                connection, client_address = sock.accept()
                print('connection from', client_address)
                self.data = struct.unpack('7f', sock.recv(7*4))
            except socket.timeout:
                pass