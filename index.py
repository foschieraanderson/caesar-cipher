from src.getData import getData
from src.postJson import postJson
from src.jsonUtils import geraJson, retornaJson
from src.decifra import decifra
from src.generateHash import generateHash

import json

def main():
    response = getData('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=')
    if response:
        print('===========================================================================')
        print("Requisição Original:")
        print("---------------------------------------------------------------------------")
        print(response)
        cifrado = response['cifrado']
        nCasas = response['numero_casas']
        res = geraJson(response)
        if res:
            decifrado = decifra(cifrado, nCasas)
            data, encoding = retornaJson('src/answer.json')
            resumo = generateHash(decifrado, encoding)
            data['decifrado'] = decifrado
            data['resumo_criptografico'] = resumo
            geraJson(data)
            print('===========================================================================')
            print("Requisição Tratada:")
            print("---------------------------------------------------------------------------")
            print(json.dumps(data))
            print('===========================================================================')
            print("Resposta do POST:")
            print("---------------------------------------------------------------------------")
            response = postJson('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=', 'src/answer.json')
            response_json = response.json()
            print(response_json)

if __name__ == '__main__':
    main()