#!/usr/bin/python -tt
from gi.repository import Gtk

class SpinUI(Gtk.Application):
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('spin-me.ui')
        
        self.w = b.get_object('window1')
        self.w.connect('destroy', lambda q: Gtk.main_quit())

        self.face = b.get_object('image1')

        self.switch = b.get_object('switch1')
        self.switch.set_active(False)
        self.switch.connect('notify::active', self.toggle_face)

        self.w.show_all()

    def toggle_face(self, *args):
        if self.switch.get_active() == False:
            self.face.set_from_icon_name('face-tired-symbolic', 50)
        else:
            self.face.set_from_icon_name('face-smile-big-symbolic', 50)


if __name__ == '__main__':
    ui = SpinUI()
    Gtk.main()
