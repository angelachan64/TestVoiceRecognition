#!/usr/bin/env python

# This program is made to test the features and functionality of buttons

import pygtk
pygtk.require('2.0')
import gtk
#import GObject
import sys

def make_button_box(parent, xpm_file, label_str):
    # make box
    box = gtk.HBox(False, 0)
    box.set_border_width(2)

    # get image
    image = gtk.Image()
    image.set_from_file(xpm_file)
    image.show()

    # label
    label = gtk.Label(label_str)
    label.show()

    # pack box
    box.pack_start(image, False, False, 3)
    box.pack_start(label, False, False, 3)
    
    box.show()
    return box

class Base:
    # CLOSES THE WINDOW WHEN YOU CLICK X
    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        print "Exiting system . . ."
        gtk.main_quit()

    def on_click(self, widget, data):
        self._repeat = True
        #gobject.timeout_add(500, self.hello, data)

    def on_release(self, widget):
        self._repeat = False
        
    def hello(self, data):
        print "%s" % data

    def __init__(self):
        # making the window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Buttons")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        # making the main body
        self.box = gtk.VBox(False, 0)

        button = gtk.Button()
        button.connect("pressed", self.on_click, "Hold me down!")
        button.connect("released", self.on_release)
        box = make_button_box(self.window, "smile.ico", "Hold me down!")
        button.add(box)
        button.show()

        self.box.pack_start(button, True, True, 0)
        self.box.show()

        # show the window
        print "Beginning system . . ."
        print sys.path
        self.window.add(self.box)
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
