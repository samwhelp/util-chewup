
class Mediator:
	app = None

	user_phrase_selected = ('', '')

	def __init__ (self):
		pass

	def init (self):
		pass

	def go_show_about (self):
		dialog = self.app.win.dialog
		dialog.go_show_alert(
			"Chewing user phrase editor",
			"About Chewup"
		)

	def go_find_user_phrase_list (self):
		return self.app.service.go_find_user_phrase_list()

	def go_add_user_phrase (self):
		dialog = self.app.win.dialog

		phrase_new, bopomofo_new = self.go_get_user_phrase_add()

		## Check empty intput
		if phrase_new == '' or bopomofo_new == '':
			dialog.go_show_info(
				"Chewing user phrase.\nPhrase: %s\nBopomofo: %s\n" % (phrase_new, bopomofo_new),
				"Empty input!"
			)
			return

		## Check exist
		rtn = self.app.service.go_lookup_user_phrase(phrase_new, bopomofo_new)

		if rtn > 0:
			dialog.go_show_info(
				"Chewing user phrase.\nPhrase: %s\nBopomofo: %s\n" % (phrase_new, bopomofo_new),
				"Exist"
			)
			return

		## go add
		rtn = self.app.service.go_add_user_phrase(phrase_new, bopomofo_new)

		print()
		print('go_add_user_phrase:', rtn, phrase_new, bopomofo_new)

		## show result dialog
		if rtn > 0:
			dialog.go_show_alert(
				"Chewing user phrase.\nPhrase: %s\nBopomofo: %s\n" % (phrase_new, bopomofo_new),
				"Add Success"
			)
			self.on_add_user_phrase_success(phrase_new, bopomofo_new)
		else:
			dialog.go_show_alert(
				"Add chewing user phrase.\nPhrase: %s\nBopomofo: %s\n" % (phrase_new, bopomofo_new),
				"Edit Failure"
			)

		return rtn

	def on_add_user_phrase_success (self, phrase_new, bopomofo_new):
		self.go_set_user_phrase_selected(phrase_new, bopomofo_new)
		self.go_refresh_user_phrase_list()


	def go_edit_user_phrase (self):
		dialog = self.app.win.dialog

		phrase_new, bopomofo_new, phrase_old, bopomofo_old = self.go_get_user_phrase_edit()


		## Should select old user phrase first
		if phrase_old == '' or bopomofo_old == '':
			dialog.go_show_info(
				"Chewing user phrase selected.\nPhrase: %s\nBopomofo: %s\n" % (phrase_old, bopomofo_old),
				"Should select old user phrase first!"
			)
			return


		## Check empty intput
		if phrase_new == '' or bopomofo_new == '':
			dialog.go_show_info(
				"Chewing user phrase input.\nPhrase: %s\nBopomofo: %s\n" % (phrase_new, bopomofo_new),
				"Should input new user phrase first on edit!"
			)
			return

		##  New Phrase should equal Old Phrase
		if phrase_new != phrase_old:
			dialog.go_show_info(
				"New Phrase: %s\nOld Phrase: %s\n" % (phrase_new, phrase_old),
				"New Phrase should equal Old Phrase!"
			)
			return

		## Check Old Phrase Exist
		rtn = self.app.service.go_lookup_user_phrase(phrase_old, bopomofo_old)

		if rtn < 1:
			dialog.go_show_info(
				"Chewing user phrase.\nOld Phrase: %s\nOld Bopomofo: %s\n" % (phrase_old, bopomofo_old),
				"Old Phrase Not Exist"
			)
			return

		## Remove Old Phrase
		rtn = self.app.service.go_remove_user_phrase(phrase_old, bopomofo_old)

		## Add New Phrase
		rtn = self.app.service.go_add_user_phrase(phrase_new, bopomofo_new)

		print()
		print('go_edit_user_phrase:', rtn, phrase_old, bopomofo_old, phrase_new, bopomofo_new)

		dialog.go_show_alert(
			"Chewing user phrase.\nOld Phrase: %s\nNew Phrase: %s\nOld Bopomofo: %s\nNew Bopomofo: %s\n" % (phrase_old, phrase_new, bopomofo_old, bopomofo_new),
			"Edit Success"
		)

		self.on_edit_user_phrase_success(phrase_new, bopomofo_new)

		return rtn

	def on_edit_user_phrase_success (self, phrase_new, bopomofo_new):
		self.go_set_user_phrase_selected(phrase_new, bopomofo_new)
		self.go_refresh_user_phrase_list()


	def go_remove_user_phrase (self):
		dialog = self.app.win.dialog

		phrase_old, bopomofo_old = self.go_get_user_phrase_remove()


		## Should select old user phrase first
		if phrase_old == '' or bopomofo_old == '':
			dialog.go_show_info(
				"Chewing user phrase selected.\nPhrase: %s\nBopomofo: %s\n" % (phrase_old, bopomofo_old),
				"Should select old user phrase first on remove!"
			)
			return

		## Check Old Phrase Exist
		rtn = self.app.service.go_lookup_user_phrase(phrase_old, bopomofo_old)

		if rtn < 1:
			dialog.go_show_info(
				"Chewing user phrase.\nOld Phrase: %s\nOld Bopomofo: %s\n" % (phrase_old, bopomofo_old),
				"Old Phrase Not Exist!"
			)
			self.go_set_user_phrase_edit('', '')
			return


		rtn = dialog.go_show_confirm(
			"Chewing user phrase selected.\nPhrase: %s\nBopomofo: %s\n" % (phrase_old, bopomofo_old),
			"Are you sure to remove user phrase?"
		)

		if (rtn == dialog.reply_no):
			return

		rtn = self.app.service.go_remove_user_phrase(phrase_old, bopomofo_old)

		print()
		print('go_remove_user_phrase_list:', rtn, phrase_old, bopomofo_old)

		## show result dialog
		if rtn > 0:
			dialog.go_show_alert(
				"Chewing user phrase.\nPhrase: %s\nBopomofo: %s\n" % (phrase_old, bopomofo_old),
				"Remove Success"
			)
			self.on_remove_user_phrase_success()
		else:
			dialog.go_show_alert(
				"Add chewing user phrase.\nPhrase: %s\nBopomofo: %s\n" % (phrase_old, bopomofo_old),
				"Remove Failure"
			)

		return rtn

	def on_remove_user_phrase_success (self):
		self.go_set_user_phrase_edit('', '')
		self.go_refresh_user_phrase_list()


	def on_yes_remove(self):
		print('on_yes_remove:')

	def on_no_remove (self):
		print('on_no_remove:')


	def go_refresh_user_phrase_list (self):
		print()
		print('go_refresh_user_phrase:')

		rtn = self.app.win.user_phrase_list.go_refresh()

		return rtn

	def go_set_user_phrase_selected (self, phrase, bopomofo):
		self.user_phrase_selected = (phrase, bopomofo)
		self.app.win.user_phrase_input.go_set_current_user_phrase_edit(phrase, bopomofo)

	def go_get_user_phrase_selected (self):
		return self.user_phrase_selected

	def go_set_user_phrase_edit (self, phrase, bopomofo):
		self.user_phrase_selected = (phrase, bopomofo)
		self.app.win.user_phrase_input.go_set_user_phrase_edit(phrase, bopomofo)

	def go_get_user_phrase_add (self):
		phrase_new, bopomofo_new = self.app.win.user_phrase_input.go_get_current_user_phrase()

		phrase_new = phrase_new.strip()
		bopomofo_new = bopomofo_new.strip()

		return (phrase_new, bopomofo_new)

	def go_get_user_phrase_edit (self):
		phrase_new, bopomofo_new = self.app.win.user_phrase_input.go_get_current_user_phrase()
		phrase_old, bopomofo_old = self.go_get_user_phrase_selected()

		phrase_new = phrase_new.strip()
		bopomofo_new = bopomofo_new.strip()
		phrase_old = phrase_old.strip()
		bopomofo_old = bopomofo_old.strip()

		return (phrase_new, bopomofo_new, phrase_old, bopomofo_old)

	def go_get_user_phrase_remove (self):
		phrase_old, bopomofo_old = self.go_get_user_phrase_selected()

		phrase_old = phrase_old.strip()
		bopomofo_old = bopomofo_old.strip()

		return (phrase_old, bopomofo_old)
