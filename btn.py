import gtk
class PyApp (gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("button")
        self.set_size_request(650, 450)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        btn1 = gtk.Button("button1")
        btn1.set_sensitive(True)
        btn1.set_size_request(80, 60)
        btn2 = gtk.Button("button2")
        btn2.set_size_request(80, 60)

        btn3 = gtk.Button(stock=gtk.STOCK_CLEAR)
        btn3.set_size_request(80, 60)
        btn3.set_tooltip_text("this is button")

        fixed = gtk.Fixed()

        fixed.put(btn1, 20, 30)
        fixed.put(btn2, 570, 30)
        fixed.put(btn3, 110, 30)

        self.set_tooltip_text("this is window")

        self.add(fixed)
        self.show_all()

PyApp()
gtk.main()
