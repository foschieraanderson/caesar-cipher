from src.getResponse import getResponse
from src.postUrl import postUrl
from src.jsonUtils import geraJson, retornaJson
from src.decifra import decifra
from src.generateHash import generateHash

import json

get_url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
post_url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='

def main():
    response = getResponse(get_url)
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
            response = postUrl(post_url, 'src/answer.json')
            response_json = response.json()
            print(response_json)

if __name__ == '__main__':
    main()