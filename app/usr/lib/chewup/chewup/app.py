
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from chewup.signal import Signal
from chewup.keybind import Keybind

from chewup.ui.win import Win
from chewup.ui.indicator import Indicator

from chewup.act.mediator import Mediator
from chewup.act.service import Service


class App:

	name = 'chewup'

	signal = None
	win = None
	indicator = None
	keybind = None

	def __init__ (self):
		pass

	def init (self):
		self.signal = signal = Signal()
		self.app = self
		signal.init()

		self.keybind = keybind = Keybind()
		keybind.app = self
		keybind.init()

		self.mediator = mediator = Mediator()
		mediator.app = self
		mediator.init()

		self.service = service = Service()
		service.app = self
		service.init()

		self.win = win = Win()
		win.app = self
		win.init()

		self.indicator = indicator = Indicator()
		indicator.app = self
		indicator.init()

	def run (self):
		Gtk.main()

	def go_show_about (self):
		#print('about:')
		self.mediator.go_show_about()

	def go_quit (self):
		Gtk.main_quit()
