import requests

def harrypotter_personaje():
    """Retorna los personajes y casas de Harry Potter"""
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)

    if response.ok:
        payload = response.json()
        personaje = input('Ingrese el nombre del personaje: ')
        personaje_encontrado = False  # Bandera para verificar si se encontró el personaje
        
        for r in range(len(payload)):
            if personaje in payload[r]['name']:
                print(f"La casa de {personaje} es: {payload[r]['house']}")
                personaje_encontrado = True  # Se encontró el personaje, establece la bandera en True
        
        if not personaje_encontrado:
            print('Casa de personaje no encontrada o no existe el personaje')
    else:
        print(f'Sucedió un error {response.status_code} obteniendo la información, mas detalles a continuación')
        print(response.text)

if __name__ == '__main__':
    harrypotter_personaje()
