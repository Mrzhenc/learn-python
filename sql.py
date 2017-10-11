import gtk
from gtk import gdk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("logo")
        self.set_size_request(800, 600)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy",gtk.main_quit)
        pixbuf = gdk.pixbuf_new_from_file("/root/workspace/EastedClient/EastedUI/bg.png")
        pixbuf1 = pixbuf.scale_simple(1280, 800, gdk.INTERP_BILINEAR)
        im = gtk.image_new_from_pixbuf(pixbuf1)
        fixed = gtk.Fixed()
        ima = gtk.Image()
        ima.set_from_file("/root/workspace/EastedClient/EastedUI/logo.png")

        _passwd_entry = gtk.Entry()
        _passwd_entry.set_editable(True)
        Passwd_label = gtk.Label("Account")
        Passwd_label.set_text(_passwd_entry.get_text())
        Passwd_label.set_no_show_all(0)
        fixed.put(im, 0, 0)
        fixed.put(Passwd_label, 35, 100)
        fixed.put(_passwd_entry, 100, 100)
        fixed.put(ima, 200, 0)

        del pixbuf, pixbuf1
        self.add(fixed)
        self.show_all()
PyApp()
gtk.main()
