import base64
class Media2B64:
    """ a class to convert online/offline media to base64"""
    __version__ = '0.1'
    def __init__(self, data):
        self.data = data

    def encode(self, data: bytes = None):
        """ convert from bytes to b64 """
        return base64.b64encode(self.data)

    def decode(self, data: bytes = None):
        """ convert b64 to bytes """
        return base6.b64decode(self.data)
