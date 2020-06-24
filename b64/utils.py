import os
import requests


class FileNotFound(Exception):
    """ Exception for file not found """

    def __init__(self):
        msg = '''
		File Not Found, please check your path, permission, and headers
		And Try Again'''
        super().__init__(msg)


def download_file(source, codes=(200, ), chunk=1024, *args, **kwargs) -> bytes:
    """ a function to download files from internet to bytes """
    file = bytes()
    try:
        r = requests.get(source, stream=True, *args, **kwargs)
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


def exists(source) -> bool:
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
