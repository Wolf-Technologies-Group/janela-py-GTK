#!/usr/bin/env python

import pygtk
import gtk

win= gtk.Window()
win.set_title('Janela teste')
win.set_size_request(500,350)
win.connect("destroy",gtk.main_quit)
win.show()
gtk.main()
