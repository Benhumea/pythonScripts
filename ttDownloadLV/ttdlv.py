# Importa la librería de manejo de errores de HTTP
import requests.exceptions

# Intenta descargar los videos
try:
    # Obtén tu "client key" y "client secret" de la consola de desarrolladores de TikTok
    CLIENT_KEY = "aw6pq0ii3ved3nox"
    CLIENT_SECRET = "59b0d9b483dc41ac515377e3a5bc62f8"

    # Solicita un "access token" a la API de TikTok
    response = requests.post("https://api.tiktok.com/oauth/token", {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": "favorite"
    })

    # Obtén el "access token" de la respuesta
    access_token = response.json()["access_token"]

    # Crea una carpeta para guardar los videos descargados
    if not os.path.exists("videos"):
        os.makedirs("videos")

    # Obtén la lista de videos que le has dado "me gusta" en tu cuenta de TikTok
    url = "https://api.tiktok.com/favorite/list"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "count": "100"  # Solicita 100 videos por página
    }

    # Realiza la solicitud a la API
    response = requests.get(url, headers=headers, params=params)

    # Obtén los datos de los videos de la respuesta
    videos = response.json()["favoriteList"]

    # Descarga cada uno de los videos con yt-dlp
    for video in videos:
        os.system(f"yt-dlp -o videos/{video['title']
