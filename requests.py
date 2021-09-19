import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(type(response))
    print(response.status_code) #200 -sucesso, 400 - nao existe, not found
    print(response.text) # class str
    print(type(response.text))
    print(response.json()) # class dict
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    print(dados_pokemon['sprites']['other'])

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # retorna_dados_cep('53625813')
    #retorna_dados_pokemon('pikachu')
    resposta = retorna_response('https://github.com/IgorEM/Melhor-Rota---Metro-da-cidade-do-Mexico---Dijkstra-')
    print(resposta)

