import requests
from pprint import pprint

def abilities(ability, pokemon_name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/move/{ability}/').json()
    except:
        return print('Error: Ability or pokemon not found')

    type = response['type']['name']
    accuracy = response['accuracy']
    effect = response['effect_entries'][0]['effect']
    learned_pokemon = response['learned_by_pokemon']
    
    for pokemon in learned_pokemon:
        if pokemon_name == pokemon['name']:
            return print(f'\n{pokemon_name} can use {ability} with {accuracy} accuracy. \n{pokemon_name} is a {type} type pokemon. \n{effect}')   
        return print(f'\n{pokemon_name} cannot use {ability}')

while True:
    input_ability = input('\nEnter ability: ').replace(' ', '-')
    pokemon = input('Enter pokemon: ').replace(' ', '-')
    abilities(input_ability, pokemon)

