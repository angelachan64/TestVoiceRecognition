#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    # CLOSES THE WINDOW WHEN YOU CLICK X
    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        print "Exiting system . . ."
        gtk.main_quit()

    # EXPERIMENTATION
    def hello(self, widget, data):
        print "Hello World! %s was pressed." % data

    # STARTING UP A NEW WINDOW
    def __init__(self):
        # making the window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Testing things out")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(100)

        # making a box to pack widgets into
        #self.box1 = gtk.HBox(False, 0)
        self.box1 = gtk.VBox(False, 0)

        # making the buttons
        self.button1 = gtk.Button("Button 1")
        self.button2 = gtk.Button("Button 2")
        self.button1.connect("clicked", self.hello, "Button 1")
        self.button2.connect("clicked", self.hello, "Button 2")
        #self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        # adding everything
        self.window.add(self.box1)
        self.box1.pack_start(self.button1, True, True, 0)
        self.box1.pack_start(self.button2, True, True, 0)
        self.box1.show()
        self.button1.show()
        self.button2.show()

        # show the window
        print "Beginning system . . ."
        self.window.show()

    def main(self):
        gtk.main()

    

#print __name__
if __name__ == "__main__":
    base = Base()
    base.main()
