
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as AppIndicator


class Indicator:
	app = None
	view = None
	indicator = None
	menu = None

	icon_name_on_win_activate = 'empty'
	icon_name_on_win_deactivate = 'folder'
	icon_name_btn_app_quit = 'application-exit'

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_menu()
		self.view = self.indicator

	def init_menu (self):

		## Menu
		self.menu = menu = Gtk.Menu()

		## Activate
		item = Gtk.MenuItem.new_with_label('Activate (<Super>+a)')
		item.connect('activate', self.on_activate_win)
		menu.append(item)

		## Fullscreen
		item = Gtk.MenuItem.new_with_label('Fullscreen (F11)')
		item.connect('activate', self.on_fullscreen_win)
		menu.append(item)

		## About
		item = Gtk.MenuItem.new_with_label('About')
		item.connect('activate', self.on_show_about)
		menu.append(item)

		## Quit
		img = Gtk.Image.new_from_icon_name(self.icon_name_btn_app_quit, 16)
		item = Gtk.ImageMenuItem.new_with_label('Quit')
		item.connect('activate', self.on_quit_app)
		item.set_image(img)
		menu.append(item)

		menu.show_all()

		## Indicator
		self.indicator = indicator = AppIndicator.Indicator.new(
			self.app.name,
			self.icon_name_on_win_activate,
			AppIndicator.IndicatorCategory.APPLICATION_STATUS
		)
		indicator.set_menu(menu)
		indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)

	def on_show_about (self, menu_item):
		self.app.go_show_about()

	def on_quit_app (self, menu_item):
		self.app.go_quit()

	def on_activate_win (self, menu_item):
		self.app.win.go_activate()

	def on_fullscreen_win (self, menu_item):
		self.app.win.go_fullscreen()

	def go_switch_icon_on_win_activate (self):
		self.indicator.set_icon(self.icon_name_on_win_activate)

	def go_switch_icon_on_win_deactivate (self):
		self.indicator.set_icon(self.icon_name_on_win_deactivate)
