"""
test api pokemonbattle
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',"trainer_token":"b02711a23abe4268791a2074371a18b5"} 

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',"trainer_token":"b02711a23abe4268791a2074371a18b5"} 

body = {
    "pokemon_id": "28014",
    "name": "men",
    "photo": "https://dolnikov.ru/pokemons/albums/012.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',"trainer_token":"b02711a23abe4268791a2074371a18b5"} 

body = {
    "pokemon_id": "28014"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')