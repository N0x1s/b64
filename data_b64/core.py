import base64
from urllib import request

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

	def download_file(self, source: str = str(), chunk: int = 1024) -> bytes:
		""" a method to download files from online to bytes """
		file = bytes()
		r = request.urlopen(source)
		while True:
			part = r.read(chunk)
			if not part:
				break
			file += part
		return file

"""
#### tests ####
b64_strings = 'dGVzdA=='
string = b'test'
image_online = 'https://upload.wikimedia.org/wikipedia/en/9/95/Test_image.jpg'
r = Media2B64().download_file(image_online)
print(r)
"""
