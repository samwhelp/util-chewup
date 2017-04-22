import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('Notify', '0.7')
from gi.repository import Notify

class Dialog:
	app = None
	view = None
	win = None

	reply_yes = Gtk.ResponseType.YES
	reply_no = Gtk.ResponseType.NO

	def prep (self, *args, **kwds):
		self.app = kwds['app']
		self.win = kwds['win']

	def init (self):
		pass

	def new_alert (self):
		return Alert()

	def go_show_alert (self, message, title='', type='dialog-information'):
		dialog = self.new_alert()
		dialog.title = title
		dialog.message = message
		dialog.type = type
		dialog.init()
		return dialog.show()

	def new_info (self):
		dialog = Info()
		dialog.win = self.win
		return dialog

	def go_show_info (self, message, title='', type=Gtk.MessageType.INFO):
		dialog = self.new_info()

		dialog.title = title
		dialog.message = message
		dialog.type = type
		dialog.init()
		return dialog.show()

	def new_confirm (self):
		dialog = Confirm()
		dialog.win = self.win
		return dialog

	def go_show_confirm (self, message, title='', run_yes=None, run_no=None, type=Gtk.MessageType.QUESTION):
		dialog = self.new_confirm()

		dialog.title = title
		dialog.message = message
		dialog.type = type
		dialog.run_yes = run_yes
		dialog.run_no = run_no
		dialog.init()
		return dialog.show()


class Alert:
	app = None
	view = None
	dialog = None

	name = 'alert'
	title = ''
	message = ''
	type = 'dialog-information'

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_dialog()
		self.view = self.dialog

	def init_dialog (self):
		Notify.init(self.name)
		self.dialog = dialog = Notify.Notification.new(self.title, self.message, self.type)

	def show (self):
		self.dialog.show()

class Info:
	app = None
	view = None
	win = None
	dialog = None

	name = 'info'
	title = ''
	message = ''
	type = Gtk.MessageType.INFO

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_dialog()
		self.view = self.dialog

	def init_dialog (self):
		self.dialog = dialog = Gtk.MessageDialog(
			self.win,
			0,
			self.type,
			Gtk.ButtonsType.OK,
			self.title
		)

		dialog.format_secondary_text(self.message)

	def show (self):
		rtn = self.dialog.run()
		self.destroy()
		return rtn

	def destroy (self):
		return self.dialog.destroy()

class Confirm:
	app = None
	view = None
	win = None
	dialog = None

	run_yes = None
	run_no = None

	name = 'info'
	title = ''
	message = ''
	type = Gtk.MessageType.INFO

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_dialog()
		self.view = self.dialog

	def init_dialog (self):
		self.dialog = dialog = Gtk.MessageDialog(
			self.win,
			0,
			Gtk.MessageType.QUESTION,
			Gtk.ButtonsType.YES_NO,
			self.title
		)

		dialog.format_secondary_text(self.message)

	def show (self):
		rtn = self.dialog.run()
		if rtn == Gtk.ResponseType.YES:
			self.on_yes()
		elif rtn == Gtk.ResponseType.NO:
			self.on_no()

		self.destroy()

		return rtn

	def destroy (self):
		return self.dialog.destroy()

	def on_yes (self):
		if self.run_yes:
			self.run_yes()

	def on_no (self):
		if self.run_no:
			self.run_no()
