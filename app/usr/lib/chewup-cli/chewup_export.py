#!/usr/bin/env python3

import sys
import argparse
import json

from chewing import userphrase

from chewup.signal import Signal


class App:
	name = 'chewup-export'

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
			self.file = open(self.file_path, 'w')
		except IOError:
			print('Error open file:', self.file_path)
			sys.exit(1)
			return

		try:
			self.run_export()
		except IOError:
			print('Error write file:', self.file_path)
			sys.exit(1)
			return
		finally:
			self.file.close()

		sys.exit(0)

	def run_export (self):
		file_type = self.file_type

		if file_type == 'default':
			self.run_export_default()
		elif file_type == 'json':
			self.run_export_json()
		else:
			print('Not support type:', file_type)

	def run_export_default (self):
		userphrase.foreach(self.run_each_default)

	def run_export_json (self):
		self.list = []
		userphrase.foreach(self.run_each_json)
		self.file.write(json.dumps(self.list))

	def run_each_default (self, phrase, bopomofo):
		self.file.write("phrase: %s\n" % phrase)
		self.file.write("bopomofo: %s\n" % bopomofo)
		self.file.write("\n")

	def run_each_json (self, phrase, bopomofo):
		item = {'phrase': phrase, 'bopomofo': bopomofo}
		self.list.append(item)


def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()
