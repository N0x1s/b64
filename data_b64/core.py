import base64
class Media2B64:
    """ a class to convert online/offline media to base64"""
    __version__ = '0.1'

    def __init__(self, source:str = str()):
        if source:
            self.source = source
            self.data = source.encode('utf-8')

    def convert_to(self, destination: str, data: bytes = None) -> bytes:
        """ a method to handle conversation between base64 and bytes  """
        f = base64.b64decode if destination == 'string' else base64.b64encode
        if data:
            return f(data)
        return f(self.data)

"""
#### tests ####
b64_strings = 'dGVzdA=='
string = b'test'
r = Media2B64().convert_to('string', b64_strings)
print(r)
"""
