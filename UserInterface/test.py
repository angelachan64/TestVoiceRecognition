import kivy

from kivy.app import App
from kivy.utils import rgba
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger, LoggerHistory
from kivy.properties import ListProperty, NumericProperty, BooleanProperty
from kivy.graphics import Color, Point, Line, PushMatrix, PopMatrix, Rotate

import re
from random import randint
from os import linesep as sep
from functools import partial
from os.path import join, abspath, dirname
from math import sin, cos, radians, degrees

class Body(BoxLayout):
    default_x = default_y = 4992
    def __init__(self, **kwargs):
        super(Body, self).__init__(**kwargs)
        self.app = App.get_running_app()
        turtle = partial(Image, size_hint=[None, None], size=[16,16],
                         pos=[self.default_x, self.default_y],
                         source=self.app.icon)
        self.turtle = turtle

class MyApp(App):
    path = abspath(dirname(__file__))
    icon = join(path, 'data', 'turtle.png')
    
    def build(self):
        return Body()

if __name__ == '__main__':
    MyApp().run()
