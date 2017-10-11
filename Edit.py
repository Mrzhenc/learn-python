import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Entry")
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_size_request(250, 200)

        fixed = gtk.Fixed()

        self.label1 = gtk.Label("usr:")
        self.label = gtk.Label("...")
        fixed.put(self.label1, 30, 40)
        fixed.put(self.label, 60, 40)

        entry = gtk.Entry()
        entry.add_events(gtk.gdk.KEY_RELEASE_MASK)
        fixed.put(entry, 60, 100)

        entry.connect("key-release-event", self.on_release)

        self.connect("destroy", gtk.main_quit)
        self.add(fixed)
        self.show_all()

    def on_release(self, widget, event):
        self.label.set_text(widget.get_text())

PyApp()
gtk.main()
