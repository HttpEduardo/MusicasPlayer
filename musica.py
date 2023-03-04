import requests
import pyaudio
import tkinter

# Definir a URL da API do Spotify
url = 'https://api.spotify.com/v1/tracks'

# Definir os parâmetros necessários
params = {
    'artist': 'Michael Jackson',
    'title': 'Thriller'
}

# Fazer a solicitação da API
response = requests.get(url, params=params)

# Obter os dados da música
data = response.json()

# Instanciar o objeto PyAudio
audio = pyaudio
