import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("window")
        self.set_size_request(650, 450)
        self.set_position(gtk.WIN_POS_CENTER)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6400))

        btn = gtk.Button("button1")
        btn.set_size_request(80, 60)

        fixed = gtk.Fixed()
        fixed.put(btn, 100, 100)

        mb = gtk.MenuBar()
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("file")
        filem.set_submenu(filemenu)

        exit = gtk.MenuItem("exit")
        exit.connect("activate", self.on_destroy)
        filemenu.append(exit)

        exit1 = gtk.MenuItem("open")
        exit1.connect("activate", self.on_destroy)
        filemenu.append(exit1)

        mb.append(filem)

        vbox = gtk.VBox(False, 3)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)
        self.add(fixed)

        self.connect("destroy", self.on_destroy)
        self.show_all()

    def on_destroy(self, widget):
        gtk.main_quit()

PyApp()
gtk.main()
