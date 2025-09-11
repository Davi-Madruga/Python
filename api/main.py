import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Pokemon {name} não encontrado")
while True:
    pokemon_name = input("\nNome pokemon: ").lower()
    pokemon_info = get_pokemon_data(pokemon_name)

    if pokemon_info:
        tipos = [t["type"]["name"] for t in pokemon_info["types"]]
        print("\n-=-=POKEMON-=-=\n")
        print(f"Nome: {pokemon_info["name"]}")
        print(f"#id: {pokemon_info["id"]}")
        print(f"Altura: {pokemon_info["height"]}")
        print(f"Peso: {pokemon_info["weight"]}")
        print("Tipos:","|".join([t["type"]["name"] for t in pokemon_info["types"]]))
