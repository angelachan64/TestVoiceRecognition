#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

def make_box(homogeneous, spacing, expand, fill, padding):
    # make the box
    box = gtk.HBox(homogeneous, spacing)

    # make the buttons
    if homogeneous:
        button = gtk.Button("Homogeneous")
    else:
        button = gtk.Button("Not homogeneous")
    box.pack_start(button, expand, fill, padding)
    button.show()

    button = gtk.Button("Spacing is %d units" % spacing)
    box.pack_start(button, expand, fill, padding)
    button.show()

    if expand:
        button = gtk.Button("Expand")
    else:
        button = gtk.Button("Don't expand")
    box.pack_start(button, expand, fill, padding)
    button.show()

    if fill:
        button = gtk.Button("Fill")
    else:
        button = gtk.Button("Don't fill")
    box.pack_start(button, expand, fill, padding)
    button.show()

    button = Button("Padding is %d units" % padding)
    box.pack_start(button, expand, fill, padding)
    button.show()

class Base:
    # CLOSES THE WINDOW WHEN YOU CLICK X
    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        print "Exiting system . . ."
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Making Repeat HBoxes")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        print "Beginning system . . ."
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
