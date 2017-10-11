import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("alignment")
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_size_request(650, 450)
        self.connect("destroy", gtk.main_quit)

        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 3)


        valign = gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(valign)

        ok = gtk.Button("OK")
        ok.set_size_request(70, 30)
        close = gtk.Button("Close")
        close.set_size_request(70, 30)

        hbox.add(ok)
        hbox.add(close)

        halign = gtk.Alignment(1, 0, 0, 0)
        halign.add(hbox)

        vbox.pack_start(halign, False, False, 3)

        self.add(vbox)

        self.show_all()

PyApp()
gtk.main()
