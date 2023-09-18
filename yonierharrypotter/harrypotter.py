import requests

def harrypotter():
    """Retorna los personajes y casas de Harry Potter"""
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)

    if response.ok:
        payload = response.json()
        for r in range(len(payload)):
            print(f"Hola, soy {payload[r]['name']} y mi casa es: {payload[r]['house']} " )
    else:
        print(f'Sucedió un error {response.status_code} obteniendo la información, mas detalles acontinuación')
        print(response.text)

if __name__ == '__main__':
    print(type(harrypotter()))