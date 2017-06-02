#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    # CLOSES THE WINDOW WHEN YOU CLICK X
    def delete_event(self, widget, event, data=None):
        print "Exiting system . . ."
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    # EXPERIMENTATION
    def hello(self, widget, data=None):
        print "Hello World"

    # STARTING UP A NEW WINDOW
    def __init__(self):
        # making the window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(100)

        # making the button
        self.button = gtk.Button("Hello World")
        self.button.connect("clicked", self.hello, None)

        # adding the button
        self.window.add(self.button)
        self.button.show()

        # show the window
        print "Beginning system . . ."
        self.window.show()

    def main(self):
        gtk.main()

    

#print __name__
if __name__ == "__main__":
    base = Base()
    base.main()
