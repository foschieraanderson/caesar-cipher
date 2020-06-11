import hashlib

def generateHash(text, encoding):
  return hashlib.sha1(text.encode(encoding)).hexdigest()