import gtk

class GameFace(gtk.Window):
    def __init__(self):
        super(GameFace, self).__init__()

        self.set_title("Game Face")
        self.set_size_request(640, 480)
        self.set_position(gtk.WIN_POS_CENTER)
        #self.connect("destroy", gtk.main_quit)
        self.__times = 0

        vbox = gtk.VBox()
        table = gtk.Table(15, 15, True)
        for i in range(15):
            for j in range(15):
                _btn = gtk.Button()
                table.attach(_btn, j, j+1, i, i+1)
                _btn.connect("clicked", self.on_setlabel)
        vbox.pack_start(table, True, True, 0)
        self.add(vbox)
        self.show_all()

    def on_setlabel(self, widget):
        if self.__times % 2 == 0:
            widget.set_label("x")
        else:
            widget.set_label("y")
        self.__times += 1


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("wu zi qi")
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_size_request(860, 720)
        self.connect("destroy", gtk.main_quit)

        vbox = gtk.VBox()

        mb = gtk.MenuBar()
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("option")
        filem.set_submenu(filemenu)

        newgame = gtk.MenuItem("New Game")
        newgame.connect("activate", self.on_newgame)
        filemenu.append(newgame)

        ahead = gtk.MenuItem("Ahead")
        ahead.connect("activate", self.on_ahead)
        filemenu.append(ahead)

        back = gtk.MenuItem("Back")
        back.connect("activate", self.on_ahead)
        filemenu.append(back)
        mb.append(filem)

        exit = gtk.MenuItem("Exit")
        exit.connect("activate", self.on_exit)
        filemenu.append(exit)

        Peo_Mac = self.add_btn("new")
        _btn = self.add_btn("old")

        fixed = gtk.Fixed()

        fixed.put(Peo_Mac, 50, 200)
        fixed.put(_btn, 50, 400)
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(fixed, False, False, 0)

        self.add(vbox)
        self.show_all()

    def on_exit(self, widget):
        print "Exit Now!!!"
        gtk.main_quit()

    def on_ahead(self, widget):
        pass

    def on_newgame(self, widget):
        md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO,
                               gtk.BUTTONS_OK_CANCEL, "Do you want to begin A \nnew Game?")
        response = md.run()
        if response == gtk.RESPONSE_OK:
            print "new game begin"
            self.gameface = GameFace()

        else:
            print "cur game continue"
        # md.destroy()

    def add_btn(self, _type):
        _btn = gtk.Button("people-vs-computer")
        _btn.set_size_request(250, 160)
        _btn.connect("clicked", self.on_newgame)
        if _type == "new":
            _btn.set_tooltip_text("new")
        else:
            _btn.set_tooltip_text("old")

        return _btn

PyApp()
gtk.main()
