import string

def decifra(cifrado, nCasas):
  decidrado = ''
  alfabeto = string.ascii_lowercase
  for letra in cifrado:
    if letra in alfabeto:
      posicao = alfabeto.find(letra)
      posicao = (posicao - int(nCasas)) %26
      decidrado = decidrado + alfabeto[posicao]
    else:
      decidrado = decidrado + letra
  return decidrado