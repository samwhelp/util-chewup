#!/usr/bin/env python3

import sys
import argparse

from chewing import userphrase

from chewup.signal import Signal


class App:
	name = 'chewup-lookup'

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
			description='Lookup chewing user phrase.'
		)

		parser.add_argument(
			'-p',
			'--phrase',
			help="input phrase ex: -p '測試'"
		)
		parser.add_argument(
			'-b',
			'--bopomofo',
			help="input bopomofo ex: -b 'ㄘㄜˋ ㄕˋ'"
		)


		self.args = args = parser.parse_args()

	def run (self):
		parser = self.args_parser
		args = self.args
		phrase = args.phrase
		bopomofo = args.bopomofo

		if phrase == None or bopomofo == None:
			parser.print_usage()
			sys.exit(1)
			return

		rtn = userphrase.lookup(phrase, bopomofo)

		print('phrase:', phrase)
		print('bopomofo:', bopomofo)
		print('lookup (', rtn, ') userphrase')

		if rtn > 0:
			sys.exit(0)
		else:
			sys.exit(1)

def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()
