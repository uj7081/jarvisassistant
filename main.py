import os
import eel
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), 'engine'))

from engine.features import *
from engine.command import *
eel.init("www")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start("index.html", mode=None, host="localhost", block=True)