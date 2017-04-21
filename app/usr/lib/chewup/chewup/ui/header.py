
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Header:
	app = None
	view = None
	header = None

	def __init__ (self):
		pass

	def init (self):
		self.init_header()
		self.view = self.header

	def init_header (self):
		self.header = header = Gtk.HeaderBar()
		header.set_show_close_button(True)
		header.props.title = self.app.win.title
