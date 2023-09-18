import requests, logging

def harrypotter():
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)

    if response.ok:
        payload = response.json()
        for r in range(len(payload)):
            print(f"Hola, soy {payload[r]['name']} y mi casa es: {payload[r]['house']} " )

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    logging.debug('Obteniendo los nombre y casas de los personajes de Harry Potter')
    harrypotter()
    logging.debug('La tarea ha finalizado correctamente')