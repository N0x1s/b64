import base64
class Media2B64:
    """ a class to convert online/offline media to base64"""
    __version__ = '0.1'

    def __init__(self, source:str = None):
        if source:
            self.source = source
            self.data = source.encode('utf-8')

    def encode(self, data: bytes = None):
        """ convert from bytes to b64 """
        if data:
            return base64.b64encode(data)
        return base64.b64encode(self.data)

    def decode(self, data: bytes = None):
        """ convert b64 to bytes """
        if data:
            return base64.b64decode(data)
        return base64.b64decode(self.data)

"""
#### tests ####
b64_strings = 'dGVzdA=='
string = 'test'
r = Media2B64(string).encode()
print(r)
"""
