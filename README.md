# BlenderRemotify
## Background
Since Blender does not handle a native socket connection to the outside, I developed one.
The original idea comes from [Merwan Achibet](http://merwanachibet.net/blog/blender-long-running-python-scripts/) and will be further developed by me to a complete addon.

## Goal
The goal is to control Blender from the outside via UDP clients and to make a kind of real-time viewer or configurator out of Blender.

The client sends JSON over UDP and Blender processes the commands, coordinates or configurations.

In addition to the Blender addon, a client application is also being developed that allows the control a camera rig in Blender via a web interface.
