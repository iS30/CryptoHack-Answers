from base64 import *

hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

bytes = bytes.fromhex(hex)

print(b64encode(bytes))