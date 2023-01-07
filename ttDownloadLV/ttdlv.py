import requests
import os

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

    # Descarga cada uno de los videos con ffmpeg
    for video in videos:
        # Crea una carpeta para guardar el video y sus subtítulos (si los hay)
        video_folder = f"videos/{video['title']}"
        if not os.path.exists(video_folder):
            os.makedirs(video_folder)
        
        # Descarga el video
        video_url = video["video"]["downloadAddr"]
        os.system(f"ffmpeg -i {video_url} -c copy {video_folder}/video.mp4")
        
        # Descarga los subtítulos (si los hay)
        subtitles_url = video["video"]["captions"]["url"]
        if subtitles_url:
            os.system(f"ffmpeg -i {subtitles_url} {video_folder}/subtitles.")
        
                # Si hay más páginas de videos, obtén los siguientes
        while response.json()["hasMore"]:
            # Obtén el ID del último video de la lista
            max_cursor = response.json()["maxCursor"]

            # Realiza la solicitud a la API para obtener la siguiente página de videos
            params["max_cursor"] = max_cursor
            response = requests.get(url, headers=headers, params=params)

            # Obtén los datos de los videos de la respuesta
            videos = response.json()["favoriteList"]

            # Descarga cada uno de los videos con ffmpeg
            for video in videos:
                # Crea una carpeta para guardar el video y sus subtítulos (si los hay)
                video_folder = f"videos/{video['title']}"
                if not os.path.exists(video_folder):
                    os.makedirs(video_folder)

                # Descarga el video
                video_url = video["video"]["downloadAddr"]
                os.system(f"ffmpeg -i {video_url} -c copy {video_folder}/video.mp4")

                # Descarga los subtítulos (si los hay)
                subtitles_url = video["video"]["captions"]["url"]
                if subtitles_url:
                    os.system(f"ffmpeg -i {subtitles_url} {video_folder}/subtitles.srt")

# Si ocurre un error de conexión a la API, muestra un mensaje de error
except requests.exceptions.ConnectionError:
    print("Error de conexión a la API de TikTok. Por favor, vuelve a intentarlo más tarde.")

# Si ocurre cualquier otro error, muestra un mensaje de error genérico
except Exception as e:
    print("Error al descargar los videos:")
