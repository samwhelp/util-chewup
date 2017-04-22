
import gi

gi.require_version('Keybinder', '3.0')
from gi.repository import Keybinder


class Keybind:
	app = None

	accelerator_name_activate = '<Super>a'
	accelerator_name_fullscreen = 'F11'
	accelerator_name_close = 'F4'

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_keybind()

	def init_keybind (self):
		Keybinder.init()
		Keybinder.bind(self.accelerator_name_activate, self.on_key_activate_win)

	def on_key_activate_win (self, accelerator_name):
		self.app.win.go_switch_activate()

	def handle_by_accelerator_name (self, accelerator_name):
		## on press [F11]
		if accelerator_name == self.accelerator_name_fullscreen:
			self.app.win.go_switch_fullscreen()
			return True

		## on press [F4]
		elif accelerator_name == self.accelerator_name_close:
				self.app.go_quit()
				return True

		return False
