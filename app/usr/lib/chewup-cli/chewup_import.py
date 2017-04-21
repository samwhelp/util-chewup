#!/usr/bin/env python3

import sys
import argparse
import json

from chewing import userphrase

from chewup.signal import Signal


class App:

	name = 'chewup-import'

	args = None
	args_parser = None

	def __init__ (self):
		pass

	def init (self):
		self.init_siginal()
		self.init_args()

	def init_siginal (self):
		self.signal = signal = Signal()
		self.app = self
		signal.init()

	def init_args (self):
		self.args_parser = parser = argparse.ArgumentParser(
			description='Export chewing user phrase.'
		)

		parser.add_argument(
			'-f',
			'--file',
			help="export file path. ex: -f 'list.txt'",
			default='list.txt'
		)

		parser.add_argument(
			'-t',
			'--type',
			help="export file type. ex: -t json",
			default='default'
		)

		self.args = args = parser.parse_args()

	def run (self):
		parser = self.args_parser
		args = self.args


		self.file_path = args.file
		self.file_type = file_type =  args.type

		try:
			self.file = open(self.file_path, 'r')
		except IOError:
			print('Error open file:', self.file_path)
			sys.exit(1)
			return

		try:
			self.run_import()
		except IOError:
			print('Error read file:', self.file_path)
			sys.exit(2)
			return
		finally:
			self.file.close()

		sys.exit(0)

	def run_import (self):
		file_type = self.file_type

		if file_type == 'default':
			self.run_import_default()
		elif file_type == 'json':
			self.run_import_json()
		else:
			print('Not support type:', file_type)

	def run_import_default (self):
		## print('run_import_default:')
		rtn = 0
		item = self.new_item()
		restart = False

		for line in self.file:

			line = line.strip()

			if line == '':
				self.import_item(item)
				item = self.new_item()
				restart = True
				continue

			cols = line.split(':', 1)

			if len(cols) < 2:
				continue

			key, val = cols

			key = key.strip().lower()
			val = val.strip()

			item[key] = val

		## make sure deal with no last empty line
		if restart:
			self.import_item(item)


	def run_import_json (self):
		print('run_import_json')
		self.content = self.file.read()
		##print(self.content)

		try:
			list = json.loads(self.content)
		except json.JSONDecodeError:
			print('Error parse json file:', self.file_path)
			sys.exit(3)
			return
		finally:
			pass

		for item in list:
			self.import_item(item)


	def new_item (self):
		return {'phrase': None, 'bopomofo': None}

	def import_item (self, item):
		phrase = item['phrase']
		bopomofo = item['bopomofo']

		if phrase != None and bopomofo !=None:
			rtn = userphrase.add(phrase, bopomofo)
			print("result:", rtn)
			print("phrase:", phrase)
			print("bopomofo:", bopomofo)
			print()


def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()
