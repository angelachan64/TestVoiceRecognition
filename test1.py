#!/usr/bin/env python

# This program shows a visual representation of the results of changing
# the homogeneous, spacing, expand, fill, and padding values when making
# buttons and packing them into boxes

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

    str = "Spacing is %d units" % spacing
    button = gtk.Button(str)
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

    str = "Padding is %d units" % padding
    button = gtk.Button(str)
    box.pack_start(button, expand, fill, padding)
    button.show()

    return box

def make_label(labelstr):
    label = gtk.Label(labelstr)
    label.show()
    return label

def make_separator():
    separator = gtk.HSeparator()
    separator.show()
    return separator

class Base:
    # CLOSES THE WINDOW WHEN YOU CLICK X
    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        print "Exiting system . . ."
        gtk.main_quit()

    def __init__(self):
        # making the window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Making Repeat HBoxes")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        # making the boxes
        self.box1 = gtk.VBox(True, 0)

        labelstr = "This program shows a visual representation of the results of "
        labelstr += "changing the homogeneous,\nspacing, expand, fill, and padding"
        labelstr += " values when making buttons and packing them into boxes."
        self.box1.pack_start(make_label(labelstr), True, True, 0)

        self.box1.pack_start(make_separator(), True, True, 0)
        
        
        labelstr = "Homogeneous, No spacing, Expand, Fill, No padding"
        self.box1.pack_start(make_label(labelstr), True, True, 0)
        
        self.box2 = make_box(True, 0, True, True, 0)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box2.show()

        self.box1.pack_start(make_separator(), True, True, 0)
        

        labelstr = "Homogeneous, 5 Spacing, Expand, Fill, No padding"
        self.box1.pack_start(make_label(labelstr), True, True, 0)

        self.box2 = make_box(True, 5, True, True, 0)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box2.show()

        self.box1.pack_start(make_separator(), True, True, 0)


        labelstr = "Homogeneous, No spacing, Expand, Fill, 5 padding"
        self.box1.pack_start(make_label(labelstr), True, True, 0)

        self.box2 = make_box(True, 0, True, True, 5)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box2.show()

        self.box1.pack_start(make_separator(), True, True, 0)


        labelstr = "Homogeneous, No spacing, Expand, Don't fill, No padding"
        self.box1.pack_start(make_label(labelstr), True, True, 0)

        self.box2 = make_box(True, 0, True, False, 0)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box2.show()

        self.box1.pack_start(make_separator(), True, True, 0)

        
        labelstr = "Not homogeneous, No spacing, Expand, Fill, No padding"
        self.box1.pack_start(make_label(labelstr), True, True, 0)
        
        self.box2 = make_box(False, 0, True, True, 0)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box2.show()

        self.box1.pack_start(make_separator(), True, True, 0)

        
        labelstr = "Not homogeneous, No spacing, Expand, Don't fill, No padding"
        self.box1.pack_start(make_label(labelstr), True, True, 0)

        self.box2 = make_box(False, 0, True, False, 0)
        self.box1.pack_start(self.box2, True, True, 0)
        self.box2.show()
        

        # show everything
        print "Beginning system . . ."
        self.window.add(self.box1)
        self.box1.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
