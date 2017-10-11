import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.connect("destroy", gtk.main_quit)
        self.set_title("sec pygtk")
        self.set_size_request(350,250)
        self.set_position(gtk.WIN_POS_MOUSE)

        self.show()

PyApp()
gtk.main()
