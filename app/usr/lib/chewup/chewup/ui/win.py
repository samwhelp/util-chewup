
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from chewup.ui.header import Header

from chewup.ui.user_phrase_input import UserPhraseInput
from chewup.ui.user_phrase_list import UserPhraseList
from chewup.ui.dialog import Dialog


class Win:
	app = None
	view = None
	win = None
	layout = None
	dialog = None

	user_phrase_input = None
	user_phrase_list = None

	title = 'Chewup'

	state_fullscreen = False
	state_activate = True

	width = 900
	height = 800

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()
		self.view = self.win
		self.init_dialog()

	def init_header (self):
		self.header = header = Header()
		header.app = self.app
		header.init()

	def init_user_phrase_input (self):
		self.user_phrase_input = user_phrase_input = UserPhraseInput()
		user_phrase_input.app = self.app
		user_phrase_input.init()

	def init_user_phrase_list (self):
		self.user_phrase_list = user_phrase_list = UserPhraseList()
		user_phrase_list.app = self.app
		user_phrase_list.init()
		user_phrase_list.go_load()

	def init_dialog (self):
		self.dialog = dialog = Dialog()
		dialog.app = self.app
		dialog.win = self.win
		dialog.init()

	def init_win (self):
		self.win = win = Gtk.Window()

		win.connect('delete-event', self.on_close_win)
		win.connect('key-press-event', self.on_key_press)
		win.connect('key-release-event', self.on_key_release)

		## set attribute
		win.set_title(self.title)
		win.resize(self.width, self.height)

		## haderbar
		self.init_header()
		win.set_titlebar(self.header.view)

		## layout
		self.layout = layout = Gtk.Grid()
		win.add(layout)


		self.init_user_phrase_input()
		layout.attach(self.user_phrase_input.view, 0, 0, 1, 1)


		self.init_user_phrase_list()
		layout.attach(self.user_phrase_list.view, 0, 1, 1, 1)


		win.show_all()


	def on_close_win (self, win, evt):
		self.go_deactivate()
		## self.app.go_quit()

		return True

	def on_key_press (self, win, evt):

		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)

		return self.app.keybind.handle_by_accelerator_name(accelerator_name)


	def on_key_release (self, win, evt):
		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)

		return False

	## fullscreen
	def is_fullscreen (self):
		return self.state_fullscreen

	def set_state_fullscreen (self, val):
		self.state_fullscreen = val

	def go_switch_fullscreen (self):
		if self.is_fullscreen():
			self.go_unfullscreen()
		else:
			self.go_fullscreen()

	def go_fullscreen (self):
		self.set_state_fullscreen(True)
		self.win.fullscreen()
		self.go_activate()

	def go_unfullscreen (self):
		self.set_state_fullscreen(False)
		self.win.unfullscreen()
		self.go_show_default()

	## activate
	def is_activate (self):
		return self.state_activate

	def set_state_activate (self, val):
		self.state_activate = val

	def go_switch_activate (self):
		if self.is_activate():
			self.go_deactivate()
		else:
			self.go_activate()

	def go_activate (self):
		self.set_state_activate(True)
		self.win.present()
		self.app.indicator.go_switch_icon_on_win_activate()
		self.go_show_default()

	def go_deactivate (self):
		self.set_state_activate(False)
		self.win.hide()
		self.app.indicator.go_switch_icon_on_win_deactivate()

	def go_show_default (self):
		self.win.move(200,200)
