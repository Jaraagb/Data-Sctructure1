import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

AUDIO_FEATURES_COLS = ['danceability', 'energy', 'speechiness', 'acousticness',
                       'instrumentalness', 'liveness', 'valence', 'tempo']

def prepare_dataset(path='spotifydataset.csv'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no fue encontrado.")

    dataset = pd.read_csv(path)
    dataset = dataset.dropna(subset=AUDIO_FEATURES_COLS)
    X = dataset[AUDIO_FEATURES_COLS]
    return dataset, X

def train_kmeans(X, dataset, n_clusters=10, save_model=True):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)

    dataset['cluster'] = kmeans.predict(X_scaled)

    if save_model:
        from pathlib import Path

        # ✅ Asegura que la ruta absoluta exista correctamente
        models_path = Path(__file__).resolve().parent  # Esto te da la carpeta actual: .../Models/
        
        # 🔧 Crea la carpeta si no existe (aunque ya debería existir por estructura)
        models_path.mkdir(parents=True, exist_ok=True)

        # ✅ Guarda los modelos en esa ruta
        with open(models_path / 'scaler.pkl', 'wb') as f:
            pickle.dump(scaler, f)
        with open(models_path / 'kmeans.pkl', 'wb') as f:
            pickle.dump(kmeans, f)

