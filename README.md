# BlenderRemotify
## Background
Since Blender does not handle a native socket connection to the outside, I developed one.
The original idea comes from [Merwan Achibet](http://merwanachibet.net/blog/blender-long-running-python-scripts/) and will be further developed by me to a complete add-on.

## Goal of this add-on
The goal is to control Blender from the outside via UDP clients and to make a kind of real-time viewer or configurator out of Blender.

The controller app sends JSON over UDP and Blender processes the commands, coordinates or configurations.

## Controller app
Additionally, I am developing an app under the name "BlenderRemotifyController", but it will not be open source.
This app is a combination of a local webserver that serves a web app. This allows a tablet or smartphone to be used as a remote control.

## Future plan
* Develop a kind of configurator in Blender:  
Configuration of geometry or shader values should be switchable from outside
* Switch between different render engines via controller app
* Use fullscreen mode in Blender
