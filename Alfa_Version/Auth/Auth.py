import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "bba5806e5db549a0817dbbd1b39c006e"
CLIENT_SECRET = "e325fa6fb8194c2591bdeb0528025853"
REDIRECT_URI = "https://6c7f-190-131-247-186.ngrok-free.app/callback"
SCOPE = "user-top-read playlist-modify-public playlist-modify-private user-read-private"

def get_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path=".cache",
        show_dialog=True
    )

# Generar URL para iniciar sesión
def get_auth_url():
    return get_spotify_oauth().get_authorize_url()

# Obtener token de acceso desde el código recibido
def get_token_from_code(code):
    sp_oauth = get_spotify_oauth()
    try:
        token_info = sp_oauth.get_access_token(code)
        return token_info['access_token']
    except Exception as e:
        print(f"❌ Error al obtener el token: {e}")
        return None

# Cliente Spotipy con el token válido usando auth_manager (✅ REQUERIDO)
def get_spotify_client_from_token(access_token):
    sp_oauth = get_spotify_oauth()
    sp_oauth._token_info = {'access_token': access_token, 'expires_at': 0}  # Forzar token manualmente
    return spotipy.Spotify(auth_manager=sp_oauth)



