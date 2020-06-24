from b64 import utils
import base64
from urllib import parse
from cached_properties import Property as property


class B64:
	""" a class to convert online/offline media to base64/text"""
	__version__ = '0.4a'

	def __init__(self, source, to='base64', *args, **kwargs):
		self.source = source
		self.to = to
		self._args, self._kwargs = args, kwargs

	def convert(self):
		""" a method to handle conversation between base64 and bytes """
		func = base64.b64encode if self.to == 'base64' else base64.b64decode
		return func(self.file_bytes)

	@property
	def file_bytes(self):
		""" cached property for file bytes """
		if isinstance(self.source, bytes):
			if not self.source:
				raise utils.FileNotFound
			return self.source
		elif parse.urlparse(self.source).scheme:
			r = utils.download_file(self.source, *self._args, **self._kwargs)
			del self._args, self._kwargs
			return r
		return utils.read_file(self.source)

	@property
	def data(self):
		return self.convert()
