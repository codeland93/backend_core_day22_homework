import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    # Process each planet's information
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')  # Get planet's English name
            mass = planet.get('mass', {}).get('massValue', 'Unknown')  # Get planet's mass value
            orbit_period = planet.get('sideralOrbit', 'Unknown')  # Get planet's orbital period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    # Extract relevant planet data and format it
    formatted_planets = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 0) * planet.get('mass', {}).get('massExponent', 0)
            orbit_period = planet.get('sideralOrbit', 0)
            formatted_planets.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})

    return formatted_planets

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


planets = fetch_planet_data()


name, mass = find_heaviest_planet(planets)


print(f"The heaviest planet is {name} with a mass of {mass:.2e} kg.")
