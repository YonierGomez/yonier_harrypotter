import requests

def harrypotter():
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)

    if response.ok:
        payload = response.json()
        for r in range(len(payload)):
            print(f"Hola, soy {payload[r]['name']} y mi casa es: {payload[r]['house']} " )

if __name__ == '__main__':
    harrypotter()