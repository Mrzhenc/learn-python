import gtk
import gobject

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()
        self.set_size_request(200, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("zhenc")
        self.connect("destroy", gtk.main_quit)
        self._init_window()


PyApp()
gtk.main()
