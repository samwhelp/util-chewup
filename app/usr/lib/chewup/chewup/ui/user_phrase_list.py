
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf


class UserPhraseList:
	app = None
	view = None
	model = None
	scroll = None
	tree = None

	column_phrase = None
	column_bopomofo = None

	column_phrase_head_title = 'Phrase'
	column_bopomofo_head_title = 'Bopomofo'

	def __init__ (self):
		pass

	def init (self):
		self.init_scroll()
		self.init_tree()
		self.scroll.add(self.tree)
		self.view = self.scroll

	def init_model (self):
		self.model = Gtk.ListStore(str, str)

	def init_scroll (self):
		self.scroll = scroll = Gtk.ScrolledWindow()
		scroll.set_hexpand(True)
		scroll.set_vexpand(True)

	def init_tree (self):

		self.init_model()
		self.init_column_phrase()
		self.init_column_bopomofo()

		self.tree = tree = Gtk.TreeView()

		tree.connect('row-activated', self.on_row_activated)
		tree.connect('key-press-event', self.on_key_press_event)

		tree.set_model(self.model)

		tree.append_column(self.column_phrase)
		tree.append_column(self.column_bopomofo)

	def init_column_phrase (self):
		self.column_phrase = column = Gtk.TreeViewColumn(self.column_phrase_head_title)

		cell_text = Gtk.CellRendererText()

		column.pack_start(cell_text, True)

		column.add_attribute(cell_text, 'text', 0)

		column.set_clickable(True)
		column.set_sort_indicator(True)

		column.set_sort_column_id(0)

	def init_column_bopomofo (self):
		self.column_bopomofo = column = Gtk.TreeViewColumn(self.column_bopomofo_head_title)

		cell_text = Gtk.CellRendererText()

		column.pack_start(cell_text, True)

		column.add_attribute(cell_text, 'text', 1)

		column.set_clickable(True)
		column.set_sort_indicator(True)

		column.set_sort_column_id(0)


	def on_row_activated (self, view, path, column):
		model = view.get_model()
		iter = model.get_iter(path)
		phrase = model.get_value(iter, 0)
		bopomofo = model.get_value(iter, 1)

		self.app.mediator.go_set_user_phrase_selected(phrase, bopomofo)

		return True

	def on_key_press_event (self, wgt, evt):
		#print('on_key_press_event:')
		pass

	def go_new_none_list (self):
		return [None, None, None]

	def go_load (self):
		self.go_load_list(self.app.mediator.go_find_user_phrase_list())

	def go_load_list (self, list):

		model = self.model

		total = 0

		for item in list:
			total += 1
			iter = model.append([item[0], item[1]])

	def go_refresh (self):
		self.init_model()
		self.go_load()

		self.tree.set_model(self.model)
		self.tree.show_all()

	def go_remove_all (self):
		model = self.tree.get_model()
		model.remove_all()
