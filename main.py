import requests
from pprint import pprint
from colorama import init, Back, Style

def abilities(ability,pokemon_name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/move/{ability}/').json()
    except:
        return print(f'{Back.RED}Ability or pokemon not found')

    learned_by_pokemon = response['learned_by_pokemon']
    power = response['power']
    priority = response['priority']
    accuracy = response['accuracy']
    
    for pokemon in learned_by_pokemon:
        if pokemon_name in pokemon['name']:
             print(f'\n{Back.BLUE}{pokemon_name.capitalize()} can learn {ability.capitalize()}')
             print(f'{Back.BLUE}Power: {power}')
             print(f'{Back.BLUE}Priority: {priority}')
             print(f'{Back.BLUE}Accuracy: {accuracy}')
             return
            
    return print(f'{Back.RED}{pokemon_name.capitalize()} can\'t learn {ability.capitalize()}')

    
def stats_abilities(pokemon_name):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/').json()
    except:
        return print(f'{Back.RED}Error: Pokemon not found')
    
    moves = response['moves']
    stats = response['stats']

    print(f'{Back.BLUE}' + pokemon_name.capitalize(), end='\n\n')
    print(f'{Back.BLUE}Abilities', end='\n\n')
    
    for move in moves:
        print (f'{Back.BLUE}-' + move['move']['name']) 
    
    print(f'\nBase stats', end='\n\n')
    
    for stat in stats:
        print(f'{Back.BLUE}' + stat['stat']['name'] + ': ' + str(stat['base_stat']))
    
while True:
    init(autoreset=True)
    print('--------------------------')
    choice = input('1. Check pokemon abilities \n2. Check pokemon stats \n3. Exit \n\nEnter option: ')
    
    if choice == '1':
        input_ability = input('\nEnter ability: ').replace(' ', '-')
        pokemon = input('\nEnter pokemon: ').replace(' ', '-')
        abilities(input_ability,pokemon)
    elif choice == '2':
        pokemon = input('\nEnter ability: ').replace(' ', '-')
        stats_abilities(pokemon)
    elif choice == '3':
        break
    else:
        print(f'{Back.RED}\nInvalid option')
    

