import requests 
import json

response = {
  "name": "Pikachu",
  "abilities": "static", 
  "abilities":"lightning-rod",  
}

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

poke_data = response.json()

print(poke_data["name"].title()) 
print(poke_data["abilities"][0]["ability"]["name"])
print(poke_data["abilities"][1]["ability"]["name"])


def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0
    for pokemon_name in pokemon_list:
        data = fetch_pokemon_data(pokemon_name)
        if data:
            weight = data['weight']
            total_weight += weight
            count += 1
    if count == 0:
        return 0
    return total_weight / count

def display_pokemon_data(pokemon_list):
    for pokemon_name in pokemon_list:
        data = fetch_pokemon_data(pokemon_name)
        if data:
            name = data['name']
            abilities = [ability['ability']['name'] for ability in data['abilities']]
            print(f"Name: {name.capitalize()}")
            print(f"Abilities: {', '.join(abilities)}")
            print()

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
average_weight = calculate_average_weight(pokemon_names)
display_pokemon_data(pokemon_names)
print(f"The average weight of the Pokémon is {average_weight} hectograms.")




