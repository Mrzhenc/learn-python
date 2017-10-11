import gtk
from gtk import gdk


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_size_request(1280, 768)
        self.set_border_width(10)
        self.set_title("my label")
        self.connect("destroy", gtk.main_quit)

        self.__fixed = gtk.Fixed()

        _note_book = gtk.Notebook()
        _note_book.set_size_request(500, 500)
        _note_book.modify_bg(gtk.STATE_NORMAL, gdk.color_parse("#FFFFFF"))
        self.__fixed.put(_note_book, 90, 10)

        combox = gtk.combo_box_new_text()
        combox.child.modify_base(gtk.STATE_NORMAL, gdk.color_parse("#880000"))
        combox.set_size_request(120, 30)
        combox.set_wrap_width(1)
        _s = self.get_size()
        for _t in _s:
            combox.append_text(_t)

        _label = gtk.Label("heheh")
        # _note_book.append_page(_fixed, _label)

        _fixed = gtk.Fixed()
        _fixed.put(combox, 10, 10)
        _f = gtk.Fixed()
        _note_book.append_page(_fixed, _label)
        _l = gtk.Label("hahaha")
        _note_book.append_page(_f, _l)
        self.add(self.__fixed)
        self.show_all()

    def get_size(self):
        _s_list = ['1920x1080', '200x300']
        return _s_list

PyApp()
gtk.main()
