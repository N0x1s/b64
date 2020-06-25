import base64
from b64 import utils
from cached_properties import Property as property
from bs4 import BeautifulSoup


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
		elif utils.fix_url(self.source, True).scheme:
			r = utils.download_file(self.source, *self._args, **self._kwargs)
			del self._args, self._kwargs
			return r
		return utils.read_file(self.source)

	@property
	def data(self):
		return self.convert()


class Tag64:
	""" convert html, css, images tags, to html(base64) """
	__version__ = '0.1'
	def __init__(self, source, tag=None, mime=None, tag_attr={}):
		self.source = source
		self.tag = tag
		self.mime = mime
		self.tag_attr = tag_attr

	@property(timeout=3600)
	def b64_string(self):
		return B64(self.source).data.decode('utf-8')

	@property
	def data_uri(self):
		return f'data:{self.mime if self.mime else ""};base64,{self.b64_string}'

	@property
	def attr(self):
		if self.tag == 'link':
			return 'href'
		elif self.tag == 'object':
			return 'data'
		return 'src'

	@property
	def html_tag(self):
		t = self.soup_contractor.new_tag(name=self.tag,
			**{self.attr:self.data_uri}, **self.tag_attr)
		return str(t) # t

	@property(general=True)
	def soup_contractor(self):
		return BeautifulSoup(features='lxml')
