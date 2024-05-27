from django.shortcuts import render
import requests


def home(request):
    return render(request, 'home.html',)


def pokemon(request):
    
    search = request.GET.get('search', '')
    
    if search:

        url = f'https://pokeapi.co/api/v2/pokemon/{search.lower()}'
        response = requests.get(url)
        if response.status_code == 200:
            pokemon = response.json()
        else:
            pokemon = None
    else:
        pokemon = None
        

    stats = {stat['stat']['name'].replace('-', '_'): stat['base_stat'] for stat in pokemon['stats']}
    total_stats = sum(stats.values())

    #porcentajes para la barra de las stats
    hp_percentage = (stats['hp']/255) * 100
    attack_percentage = (stats['attack'] / 190) * 100
    defense_percentage = (stats['defense'] / 230) * 100
    special_attack_percentage = (stats['special_attack'] / 194) * 100
    special_defense_percentage = (stats['special_defense'] / 230) * 100
    speed_percentage = (stats['speed'] / 180) * 100
    total_percentage = (total_stats / 720) * 100

    types = [types['type']['name'] for types in pokemon['types']]

    url_species = pokemon['species']['url']
    response_species = requests.get(url_species)
    data_species = response_species.json()

    pokemon_data = {
        'name' : pokemon['name'],
        'Id' : pokemon['id'],
        'image' : pokemon['sprites']['other']['official-artwork']['front_default'],
        'color': data_species['color']['name'],
        'types' : types,
        'stats' : stats,
        'total' : total_stats,
        'hp_percentage': hp_percentage,
        'attack_percentage': attack_percentage,
        'defense_percentage': defense_percentage,
        'special_attack_percentage': special_attack_percentage,
        'special_defense_percentage': special_defense_percentage,
        'speed_percentage': speed_percentage,
        'total_percentage': total_percentage,
    }

    return render(request, 'pokemon.html', {'pokemon':pokemon_data})
    





