import pandas as pd
from spotipy.exceptions import SpotifyException
from typing import Dict, List, Any

def get_top_artists_and_tracks(sp, limit: int = 20, time_range: str = 'medium_term') -> Dict[str, List[Dict[str, Any]]]:
    result = {"tracks": [], "artists": []}

    try:
        # Top Tracks
        top_tracks_data = sp.current_user_top_tracks(limit=limit, time_range=time_range)
        result["tracks"] = [{
            "name": track["name"],
            "id": track["id"],
            "popularity": track["popularity"],
            "artists": [artist["name"] for artist in track["artists"]],
            "album": track["album"]["name"],
            "image_url": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
            "spotify_url": track["external_urls"]["spotify"]
        } for track in top_tracks_data.get("items", [])]

        # Top Artists
        top_artists_data = sp.current_user_top_artists(limit=limit, time_range=time_range)
        result["artists"] = [{
            "name": artist["name"],
            "id": artist["id"],
            "genres": artist.get("genres", []),
            "popularity": artist["popularity"],
            "followers": artist["followers"]["total"],
            "image_url": artist["images"][0]["url"] if artist["images"] else None,
            "spotify_url": artist["external_urls"]["spotify"]
        } for artist in top_artists_data.get("items", [])]

        print(f"✅ Se obtuvieron {len(result['tracks'])} canciones y {len(result['artists'])} artistas más escuchados.")
        return result

    except SpotifyException as e:
        print(f"❌ Error al obtener datos desde Spotify: {e}")
        return result
