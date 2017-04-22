#!/usr/bin/env python3

import sys
import argparse

from chewing import userphrase

from chewup.signal import Signal


class App:
	name = 'chewup-dump'

	args = None
	args_parser = None

	def init (self):
		self.init_siginal()
		self.init_args()

	def init_siginal (self):
		self.signal = signal = Signal()
		self.app = self
		signal.init()

	def init_args (self):
		self.args_parser = parser = argparse.ArgumentParser(
			description='Dump chewing user phrase.'
		)

		self.args = args = parser.parse_args()

	def run (self):
		parser = self.args_parser
		args = self.args

		userphrase.foreach(self.run_each)

		sys.exit(0)

	def run_each (self, phrase, bopomofo):
		print('phrase:', phrase)
		print('bopomofo:', phrase)
		print()

	def run_find_alld (self):
		parser = self.args_parser
		args = self.args

		list = userphrase.find_all()

		##print(list)

		for item in list:
			print('phrase:', item[0])
			print('bopomofo:', item[1])
			print()

		sys.exit(0)


def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()
