def get_user_info(sp):
    return sp.current_user()

def get_top_tracks(sp, limit=50, time_range='medium_term'):
    tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    return tracks.get("items", [])

def get_top_artists(sp, limit=20, time_range='medium_term'):
    artists = sp.current_user_top_artists(limit=limit, time_range=time_range)
    return artists.get("items", [])

