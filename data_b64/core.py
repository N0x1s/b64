import base64
from urllib import request
from urllib import parse

class Media2B64:
	""" a class to convert online/offline media to base64"""
	__version__ = '0.2'

	def __init__(self, source:str = str()):
		if source:
			self.source = source
			self.data = source.encode('utf-8')

	def convert_to(self, destination: str, data: bytes = bytes()) -> bytes:
		""" a method to handle conversation between base64 and bytes  """
		f = base64.b64decode if destination == 'string' else base64.b64encode
		if data:
			return f(data)
		return f(self.data)

	def download_file(self, source: str, chunk: int = 1024) -> bytes:
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

	def read_file(self, source: str) -> bytes:
		""" read local file bytes """
		if not source:
			source = self.source
		with open(source, 'rb') as fobj:
			return fobj.read()

	def detect_type(self, source: str or bytes) -> bool:
		"""a method to detect the source type"""
		if isinstance(source, bytes):
			return 'bytes'
		elif parse.urlparse(source).scheme:
			return 'remote'
		return 'local'


#### tests ####
b64_strings = 'dGVzdA=='
string = b'test'
image_online = 'https://upload.wikimedia.org/wikipedia/en/9/95/Test_image.jpg'
image_local = 'Test_image.jpg'
r = Media2B64().detect_type(image_local)
print(r)
