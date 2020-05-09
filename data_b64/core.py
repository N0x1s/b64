import os
import base64
from urllib import request
from urllib import parse
class FileNotFound(Exception):
	""" Exception for file not found """
	def __init__(self):
		msg = '''
		File Not Found, please check your path, permission, and headers
		And Try Again'''
		super().__init__(msg)

class Media2B64:
	""" a class to convert online/offline media to base64"""
	__version__ = '0.3a'

	def __init__(self, source:str = str(), *args, **kw):
		if source:
			if not self._exists(source):
				raise FileNotFound
			self.dtype = self._detect_type(source)
			self.data = self.read_data(source, *args, **kw)

	def _transform(self, dest: str = 'base64', data: bytes = bytes()) -> bytes:
		""" a method to handle conversation between base64 and bytes
		destination parameter takes:
		string to convert from base64 to string
		b64, anything else to convert from bytes to base64"""
		f = base64.b64decode if dest == 'string' else base64.b64encode
		if data:
			return f(data)
		return f(self.data)

	def convert_to(self, dest: str = 'base64', source=None, *args, **kwargs):
		"""the function that the user call with the data"""
		if source:
			dtype = self._detect_type(source)
			func = self._pickup_method(dtype)
			return self._transform(data=func(source), *args, **kwargs)
		return self._transform(data=self.data, *args, **kwargs)

	def read_data(self, source: str or bytes, **kw) -> bytes:
		""" a method to automatically read bytes based on the source """
		return self._pickup_method(self.dtype)(source, **kw)

	def _download_file(self, source: str, chunk: int = 1024) -> bytes:
		""" a method to download files from online to bytes """
		file = bytes()
		if not source:
			source = self.source
		r = request.urlopen(source)
		while True:
			part = r.read(chunk)
			if not part:
				break
			file += part
		return file

	def _read_file(self, source: str) -> bytes:
		""" read local file bytes """
		if not source:
			source = self.source
		with open(source, 'rb') as fobj:
			return fobj.read()


	def _detect_type(self, source: str or bytes) -> str:
		""" a method that detect data type """
		if not source and not isinstance(source, bytes):
			source = self.source
		if isinstance(source, bytes):
			return 'bytes'
		elif parse.urlparse(source).scheme:
			return 'remote'
		return 'local'

	def _pickup_method(self, dtype: str or bytes):
		"""a method to pickup the right function for the data type"""
		dtype = dtype if dtype else self.dtype

		if dtype == 'remote':
			return self._download_file
		elif dtype == 'local':
			return self._read_file
		return bytes

	def _exists(self, source: str or bytes, code: list = range(200,301)) -> bool:
		""" check if the source exists """
		dtype = self._detect_type(source)
		if dtype == 'local':
			return os.path.exists(source) and os.path.isfile(source)
		elif dtype == 'remote':
			try:
				r = request.urlopen(source)
			except Exception as e:
				return False
			return r.status in code
		return bool(source)
