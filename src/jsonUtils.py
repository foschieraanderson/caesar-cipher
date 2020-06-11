import json

def geraJson(lista):
        with open('src/answer.json', 'w') as f:
            json.dump(lista, f)
            return True

def retornaJson(file):
    with open(file, 'r') as arq:
        data = json.load(arq)
        encoding = arq.encoding
        return data, encoding