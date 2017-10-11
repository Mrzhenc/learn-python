import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_position(gtk.WIN_POS_CENTER)
        self.set_size_request(250, 200)
        self.set_title("ComboBox")
        self.connect("destroy", gtk.main_quit)

        cb = gtk.combo_box_new_text()
        cb.connect("changed", self.on_changed)

        cb.append_text('zhenc')
        cb.append_text('liupp')

        fixed = gtk.Fixed()
        fixed.put(cb, 50, 30)
        self.label = gtk.Label("-")
        fixed.put(self.label, 50, 140)

        self.add(fixed)
        self.show_all()

    def on_changed(self, widget):
        self.label.set_label(widget.get_active_text())



PyApp()
gtk.main()

