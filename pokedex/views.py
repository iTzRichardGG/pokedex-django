from django.shortcuts import render
import requests


def home(request):
    return render(request, 'home.html',)


def pokemon(request):
    
    search = request.GET.get('search', '') #obtener el nombre del pokemon

    url = f'https://pokeapi.co/api/v2/pokemon/{search.lower()}' #se obtienen los datos del pokemon mediante la api
    response = requests.get(url) #se hace la peticion a la api mediante la libreria requests
    if response.status_code == 200:  
        pokemon = response.json() #si la peticion fue exitosa se obtiene el json de la url 


    # mediante un bucle se recorren los distintos diccionarios correspondiente a cada estadistica que contiene su nombre y su valor
    # se crea un diccionario con el nombre y el valor de cada estadistica
    # se remplazo el guion por un guion bajo para defense-attack y defense-defense, no se pueden usar guiones en los nombres de las variables
    stats = {stat['stat']['name'].replace('-', '_'): stat['base_stat'] for stat in pokemon['stats']} 
    total_stats = sum(stats.values()) 

    #porcentajes para la barra de las stats
    hp_percentage = (stats['hp']/200) * 100
    attack_percentage = (stats['attack'] / 200) * 100
    defense_percentage = (stats['defense'] / 200) * 100
    special_attack_percentage = (stats['special_attack'] / 200) * 100
    special_defense_percentage = (stats['special_defense'] / 200) * 100
    speed_percentage = (stats['speed'] / 200) * 100
    total_percentage = (total_stats / 700) * 100

    # Se buscan los tipos en el diccionario de tipos mediante un bucle y se guardan en una lista
    types = [types['type']['name'] for types in pokemon['types']]

    #se obtiene la url de 'species' y se hace una peticion a la api para obtener el json de la url
    #en el json se encuentra el color del pokemon
    url_species = pokemon['species']['url']
    response_species = requests.get(url_species)
    data_species = response_species.json()

    #se crea un diccionario con todos los datos del pokemon, el cual sera para acceder a los datos en las plantillas
    pokemon_data = {
        'name' : pokemon['name'],
        'Id' : pokemon['id'],
        'image' : pokemon['sprites']['other']['official-artwork']['front_default'],
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
        'color': data_species['color']['name'],
    }

    return render(request, 'pokemon.html', {'pokemon':pokemon_data})
    





