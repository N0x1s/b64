import os
import requests

class FileNotFound(Exception):
	""" Exception for file not found """

	def __init__(self):
		msg = '''
		File Not Found, please check your path, permission, and headers
		And Try Again'''
		super().__init__(msg)


def download_file(source, codes=None, chunk=1024, *args, **kwargs) -> bytes:
	""" a function to download files from internet to bytes """
	if codes is None:
		codes = range(100, 309)
	file = bytes()
	try:
		r = requests.get(fix_url(source), stream=True, *args, **kwargs)
	except Exception as e:
		raise FileNotFound
	if r.status_code not in codes:
		raise FileNotFound
	while True:
		r.raw.decode_content = True
		part = r.raw.read(chunk)
		if not part:
			break
		file += part
	return file


def read_file(source: str) -> bytes:
	""" read local file bytes """
	if os.path.exists(source) and os.path.isfile(source):
		with open(source, 'rb') as fobj:
			return fobj.read()
	raise FileNotFound


def fix_url(url, parse=False):
	if parse:
		return requests.utils.urlparse(url)
	if url.startswith('//'):
		return f'https:{url}'
	return url
