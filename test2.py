#!/usr/bin/env python

# This program was made to practice using tables

import pygtk
pygtk.require('2.0')
import gtk

def make_label(label_str):
    label = gtk.Label(label_str)
    label.show()

    return label

def make_button(button_str):
    button = gtk.Button(button_str)
    button.connect("clicked", hello, button_str)
    button.show()
    
    return button

def hello(widget, data):
    print "%s was pressed." % data

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
        self.window.set_title("Tables")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        # making the table
        table = gtk.Table(rows=9, columns=5, homogeneous=True)
        
        table.attach(make_label("This is a table"), 0, 5, 0, 1)

        table.attach(make_label("5 buttons"), 0, 5, 1, 2)
        x_connect = 0
        count = 1
        while(count <= 5):
            table.attach(make_button("Button %d" % count), x_connect, x_connect + 1, 2, 3)
            count += 1
            x_connect += 1

        table.attach(make_label("1, 3, 1 spaces"), 0, 5, 3, 4)
        x_connect = 0
        count = 9
        table.attach(make_button("Button 6"), 0, 1, 4, 5)
        table.attach(make_button("Button 7"), 1, 4, 4, 5)
        table.attach(make_button("Button 8"), 4, 5, 4, 5)

        table.attach(make_label("4, 1 spaces"), 0, 5, 5, 6)
        count = 11
        table.attach(make_button("Button 9"), 0, 4, 6, 7)
        table.attach(make_button("Button 10"), 4, 5, 6, 7)

        separator = gtk.HSeparator()
        separator.show()
        table.attach(separator, 0, 5, 7, 8)

        quit_button = make_button("Quit")
        quit_button.connect_object("clicked", gtk.Widget.destroy, self.window)
        table.attach(quit_button, 0, 5, 8, 9)
        
        # show everything
        print "Beginning system . . ."
        self.window.add(table)
        table.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
