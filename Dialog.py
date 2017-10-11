import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Dialog")
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_size_request(300, 250)
        self.connect("destroy", gtk.main_quit)

        button = gtk.Button("About")
        button.connect("clicked", self.on_about)
        button.set_size_request(80, 30)

        fixed = gtk.Fixed()
        fixed.put(button, 210, 210)

        self.add(fixed)
        self.show_all()

    def on_about(self, widget):
        about = gtk.AboutDialog()
        about.set_program_name("Battery")
        about.set_version("9.1.0.19")
        about.set_copyright("(c) Jay Chao")
        about.set_website("http://www.zhenchao.com")
        about.run()
        about.destroy()

PyApp()
gtk.main()
