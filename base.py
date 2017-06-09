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
        self.window.set_border_width(10)

        # making a box to pack widgets into
        #self.box1 = gtk.HBox(False, 0)
        self.box1 = gtk.VBox(False, 0)
        self.box2 = gtk.HBox(True, 10)
        box3 = gtk.HBox(True, 0)
        # This means homogeneous=False (not all buttons same size)
        # and spacing=0 (no spaces between objects)

        # making labels
        self.label1 = gtk.Label("Spacing")
        label2 = gtk.Label("Padding")
        self.label1.set_alignment(0, 0)
        label2.set_alignment(0, 0)
        # makes labels left aligned
        # can use self.name or just name
        separator = gtk.HSeparator()
        
        # making the buttons
        self.button1 = gtk.Button("Hello")
        self.button2 = gtk.Button("Blah blah blah")
        self.button3 = gtk.Button("?")
        self.button4 = gtk.Button("test")
        self.button1.connect("clicked", self.hello, "Hello")
        self.button2.connect("clicked", self.hello, "Blah blah blah")
        self.button3.connect("clicked", self.hello, "?")
        self.button3.connect_object("clicked", gtk.Widget.destroy, self.window)
        #self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        # adding everything
        self.window.add(self.box1)
        self.box1.pack_start(self.label1, True, True, 0)
        
        self.box2.pack_start(self.button1, True, False, 0)
        self.box2.pack_start(self.button2, True, False, 0)
        self.box2.pack_start(self.button3, True, False, 0)
        
        self.box1.pack_start(self.box2, True, True, 0)
        
        self.box1.pack_start(separator, True, True, 0)
        self.box1.pack_start(label2, True, True, 0)
        
        #box3.pack_start(self.button1, True, False, 0)
        #box3.pack_start(self.button2, True, False, 0)
        #box3.pack_start(self.button3, True, False, 0)
        box3.pack_start(self.button4, True, False, 0)
        # You can't add buttons that have already been packed
        
        self.box1.pack_start(box3, True, True, 0)
        # use pack_end() if you want to pack in the opposite direction
        # use expand= and fill= to determine certain packing outcomes
        # The first param is the child
        # The second param is expand=True (will expand to fill space)
        # Third param is fill=True (will fill space with content)
        # Fourth param is padding=0 (no space on either side of obj)
        self.box1.show()
        self.box2.show()
        box3.show()
        self.label1.show()
        self.button1.show()
        self.button2.show()
        self.button3.show()
        label2.show()
        separator.show()
        self.button4.show()

        # show the window
        print "Beginning system . . ."
        self.window.show()

    def main(self):
        gtk.main()

    

#print __name__
if __name__ == "__main__":
    base = Base()
    base.main()
