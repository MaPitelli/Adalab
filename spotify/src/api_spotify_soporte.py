#%%
import spotipy
import pandas as pd
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()
# %%
def credenciales():
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")

    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=credenciales)

    return sp
# %%
def preparamos_url(link):
    return link.split('/')[-1].split('?')[0]
# %%
def extraer_canciones(conexion, playlist_URI):
    numero_canciones = conexion.playlist_tracks(playlist_URI)['total']
    numero_canciones = int(str(numero_canciones + 100)[0])

    offset = 0
    all_data = []

    for _ in range (numero_canciones):
        resultados_iteracion = conexion.playlist_tracks(playlist_URI, offset=offset)['items']
        all_data.extend(resultados_iteracion)
        offset += 100 

    return all_data
# %%
def limpiar_datos(lista_canciones):
    basic_info = {'song':[],
              'artist':[],
              'date':[],
              'explicit':[],
              'uri_cancion':[],
              'popularity':[],
              'usuario':[],
              'links':[],
              'duracion':[]}
    
    for cancion in lista_canciones:
        basic_info['song'].append(cancion['track']['name'])
        basic_info['date'].append(cancion['added_at'])
        basic_info['explicit'].append(cancion['track']['explicit'])
        basic_info['uri_cancion'].append(cancion['track']['uri'])
        basic_info['popularity'].append(cancion['track']['popularity'])
        basic_info['usuario'].append(cancion['added_by']['id'])
        basic_info['links'].append(cancion['track']['external_urls']['spotify'])
        basic_info['duracion'].append(cancion['track']['duration_ms'])

        lista_artistas = []
        for artista in cancion['track']['artists']:
            lista_artistas.append(artista['name'])
        basic_info['artist'].append(lista_artistas)

    df_canciones = pd.DataFrame(basic_info)
    df_canciones.to_csv('datos/canciones_spotify.csv') 

    return df_canciones
# %%
def sacar_caracteristicas(dataframe_canciones, conexion):

    lista_uri_canciones = dataframe_canciones["uri_cancion"].unique().tolist()

    features =[]

    for cancion in lista_uri_canciones:
        features.append(conexion.audio_features(cancion))

    df_caract = pd.DataFrame(features)
    df_caract = df_caract[0].apply(pd.Series)

    final = dataframe_canciones.merge(df_caract, left_on="uri_cancion", right_on="uri", how="inner")

    # Guardar el DataFrame limpio en un archivo CSV con nombre personalizado
    final.to_csv("datos/datos_spotify.csv")
    return final