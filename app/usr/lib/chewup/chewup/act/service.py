
from chewing import userphrase

class Service:
	app = None

	def __init__ (self):
		pass

	def init (self):
		pass

	def go_find_user_phrase_list (self):
		return userphrase.find_all()

	def go_lookup_user_phrase (self, phrase, bopomofo):
		return userphrase.lookup(phrase, bopomofo)

	def go_add_user_phrase (self, phrase, bopomofo):
		return userphrase.add(phrase, bopomofo)

	def go_remove_user_phrase (self, phrase, bopomofo):
		return userphrase.remove(phrase, bopomofo)
