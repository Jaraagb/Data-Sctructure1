import pandas as pd
import time
from spotipy.exceptions import SpotifyException

def extract_audio_features(sp, tracks):
    track_ids = [track["id"] for track in tracks if track and "id" in track]
    features_list = []

    try:
        for i in range(0, len(track_ids), 100):
            batch = track_ids[i:i+100]
            try:
                features = sp.audio_features(tracks=batch)
                if features:
                    for f in features:
                        if f is not None:
                            features_list.append(f)
            except SpotifyException as e:
                print(f"❌ Error al solicitar audio_features (batch): {e}")
                continue
            time.sleep(0.2)  # prevenir rate limiting

        if not features_list:
            print("❌ No se pudieron obtener características de audio.")
            return pd.DataFrame(), []

        df = pd.DataFrame(features_list)
        return df, track_ids

    except Exception as e:
        print(f"❌ Error general extrayendo audio features: {e}")
        return pd.DataFrame(), []
