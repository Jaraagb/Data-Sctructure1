from flask import Flask, redirect, request, session, render_template, url_for, jsonify
from Auth.Auth import get_auth_url, get_token_from_code, get_spotify_client_from_token
from Data.UserData import get_user_info
from Data.SongAtribute import extract_audio_features
from Data.Track import get_top_artists_and_tracks
from Models.ClusterTraining import prepare_dataset
from Recommender.Recomend import recommend_by_genres
from Playlists.Playlist_Functions import get_next_playlist_name, create_playlist_and_add_tracks
import pickle
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "e325fa6fb8194c2591bdeb0528025853"  # Cambiar en producción

# Cargar modelos entrenados


basedir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(basedir, 'Models', 'scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)
with open(os.path.join(basedir, 'Models', 'kmeans.pkl'), 'rb') as f:
    kmeans = pickle.load(f)

# Dataset con clustering
dataset, _ = prepare_dataset()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return redirect(get_auth_url())

@app.route("/callback")
def callback():
    code = request.args.get('code')
    access_token = get_token_from_code(code)
    if not access_token:
        return "❌ No se pudo obtener el token de acceso"

    session['access_token'] = access_token
    sp = get_spotify_client_from_token(session.get("access_token"))
    user = sp.current_user()
    return redirect(url_for('recomendar', user_name=user['display_name']))

from Data.Track import get_top_artists_and_tracks  # asegúrate de importar la función

@app.route('/recomendar')
def recomendar():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('login'))

    sp = get_spotify_client_from_token(access_token)
    user = get_user_info(sp)
    
    # Top artistas y canciones
    top_data = get_top_artists_and_tracks(sp, limit=10)
    top_tracks = top_data['tracks']
    top_artists = top_data['artists']

    return render_template(
        'index.html',
        user_name=user['display_name'],
        top_tracks=top_tracks,
        top_artists=top_artists
    )

@app.route('/recommendations')
def recommendations():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('login'))

    sp = get_spotify_client_from_token(access_token)
    user = get_user_info(sp)

    genre_param = request.args.get('genre', 'aleatorio')
    genre_list = [g.strip() for g in genre_param.split(',')] if genre_param != 'aleatorio' else []

    # Obtener perfil musical
    music_profile = get_top_artists_and_tracks(sp)
    artists = music_profile.get("artists", [])

    if not artists:
        return "❌ No se pudieron obtener tus artistas top.", 400

    # Extraer información de artistas
    from Recommender.Recomend import extract_top_artists, recommend_by_genres, recommend_by_popularity
    artist_profiles = extract_top_artists({"items": artists})

    # Filtrar artistas por género o popularidad
    if genre_list:
        filtered_artists = recommend_by_genres(artist_profiles, genre_list)
    else:
        filtered_artists = recommend_by_popularity(artist_profiles)

    # Formatear recomendaciones para la plantilla HTML
    recs = []
    for artist in filtered_artists:
        spotify_url = artist.get("spotify_url", "")
        print(f"🎵 URL de Spotify: {spotify_url}")  # Debugging
        recs.append({
            "title": artist["name"],
            "artist": ", ".join(artist.get("genres", [])) or "Sin género",
            "image_url": artist.get("image", ""),
            "spotify_url": spotify_url,
            "id": artist.get("id", "")
        })

    return render_template(
        "recommendations.html",
        recommendations=recs,
        track_ids=[r['id'] for r in recs],
        user=user
    )


@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('login'))

    sp = get_spotify_client_from_token(session.get("access_token"))
    user_id = get_user_info(sp)['id']
    track_ids = request.json.get('track_ids', [])

    playlist_info = create_playlist_and_add_tracks(sp, user_id, track_ids, get_next_playlist_name(sp, user_id))
    return jsonify(playlist_info)

if __name__ == '__main__':
    app.run(debug=True)

