
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class UserPhraseInput:
	app = None
	view = None
	header = None

	btn_add = None
	btn_remove = None
	btn_refresh = None

	def __init__ (self):
		pass

	def init (self):
		self.init_button()
		self.view = self.layout

	def init_button (self):
		##self.box = box = Gtk.ButtonBox.new(Gtk.Orientation.HORIZONTAL)
		self.layout = layout = Gtk.Grid()

		## layout_add
		self.box_ipt_add = box_ipt_add = Gtk.Box()
		layout.attach(box_ipt_add, 0, 0, 1, 1)

		self.lbl_phrase_add = lbl_phrase_add = Gtk.Label('Phrase: ')
		box_ipt_add.add(lbl_phrase_add)

		self.ipt_phrase_add = ipt_phrase_add = Gtk.Entry()
		box_ipt_add.add(ipt_phrase_add)

		self.lbl_bopomofo_add = lbl_bopomofo_add = Gtk.Label('Bopomofo: ')
		box_ipt_add.add(lbl_bopomofo_add)

		self.ipt_bopomofo_add = ipt_bopomofo_add = Gtk.Entry()
		box_ipt_add.add(ipt_bopomofo_add)

		self.box_btn_add = box_btn_add = Gtk.Box()
		layout.attach(box_btn_add, 1, 0, 1, 1)

		self.btn_add = btn_add = Gtk.Button('Add')
		btn_add.connect('clicked', self.on_btn_add_clicked)
		box_btn_add.add(btn_add)

		## layout_edit
		self.box_ipt_edit = box_ipt_edit = Gtk.Box()
		layout.attach(box_ipt_edit, 0, 1, 1, 1)

		self.lbl_phrase_edit = lbl_phrase_edit = Gtk.Label('Phrase: ')
		box_ipt_edit.add(lbl_phrase_edit)

		self.ipt_phrase_edit = ipt_phrase_edit = Gtk.Entry()
		ipt_phrase_edit.set_editable(False)
		ipt_phrase_edit.set_sensitive(False)
		box_ipt_edit.add(ipt_phrase_edit)

		self.lbl_bopomofo_edit = lbl_bopomofo_edit = Gtk.Label('Bopomofo: ')
		box_ipt_edit.add(lbl_bopomofo_edit)

		self.ipt_bopomofo_edit = ipt_bopomofo_edit = Gtk.Entry()
		ipt_bopomofo_edit.set_editable(False)
		ipt_bopomofo_edit.set_sensitive(False)
		box_ipt_edit.add(ipt_bopomofo_edit)

		self.box_btn_edit = box_btn_edit = Gtk.Box()
		layout.attach(box_btn_edit, 1, 1, 1, 1)

		self.btn_edit = btn_edit = Gtk.Button('Edit')
		btn_edit.connect('clicked', self.on_btn_edit_clicked)
		box_btn_edit.add(btn_edit)

		self.btn_remove = btn_remove = Gtk.Button('Remove')
		btn_remove.connect('clicked', self.on_btn_remove_clicked)
		box_btn_edit.add(btn_remove)


		## layout_refresh
		self.box_btn_refresh = box_btn_refresh = Gtk.Box()
		layout.attach(box_btn_refresh, 1, 2, 1, 1)

		self.btn_refresh = btn_refresh = Gtk.Button('Refresh')
		btn_refresh.connect('clicked', self.on_btn_refresh_clicked)
		box_btn_refresh.add(btn_refresh)

		#self.btn_test = btn_test = Gtk.Button('Test')
		#btn_test.connect('clicked', self.on_btn_test_clicked)
		#box.add(btn_test)

	def on_btn_add_clicked (self, btn):
		self.app.mediator.go_add_user_phrase()

	def on_btn_edit_clicked (self, btn):
		self.app.mediator.go_edit_user_phrase()

	def on_btn_remove_clicked (self, btn):
		self.app.mediator.go_remove_user_phrase()

	def on_btn_refresh_clicked (self, btn):
		self.app.mediator.go_refresh_user_phrase_list()

	def go_get_user_phrase_add (self):
		phrase = self.ipt_phrase_add.get_text()
		bopomofo = self.ipt_bopomofo_add.get_text()
		return (phrase, bopomofo)

	def go_set_user_phrase_add (self, phrase, bopomofo):
		self.ipt_phrase_add.set_text(phrase)
		self.ipt_bopomofo_add.set_text(bopomofo)

	def go_get_user_phrase_edit (self):
		phrase = self.ipt_phrase_edit.get_text()
		bopomofo = self.ipt_bopomofo_edit.get_text()
		return (phrase_old, bopomofo_old)

	def go_set_user_phrase_edit (self, phrase, bopomofo):
		self.ipt_phrase_edit.set_text(phrase)
		self.ipt_bopomofo_edit.set_text(bopomofo)

	def go_get_current_user_phrase (self):
		phrase = self.ipt_phrase_add.get_text()
		bopomofo = self.ipt_bopomofo_add.get_text()
		return (phrase, bopomofo)

	def go_set_current_user_phrase_edit (self, phrase, bopomofo):
		self.ipt_phrase_add.set_text(phrase)
		self.ipt_bopomofo_add.set_text(bopomofo)
		self.ipt_phrase_edit.set_text(phrase)
		self.ipt_bopomofo_edit.set_text(bopomofo)
