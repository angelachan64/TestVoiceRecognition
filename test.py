import os
import pyaudio
import speech_recognition as sr
from pocketsphinx import LiveSpeech
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

for phrase in LiveSpeech():
    print phrase
