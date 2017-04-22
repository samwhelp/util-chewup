
import signal

class Signal:
	app = None

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_signal()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		signal.signal(signal.SIGINT, signal.SIG_DFL)
