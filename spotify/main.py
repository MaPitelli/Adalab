#%%
from src import api_spotify_soporte as api
# %%
sp = api.credenciales()
sp
# %%
uri_playlist = api.preparamos_url('https://open.spotify.com/playlist/6okYm53vzDoT4eiGI1l1Xe?si=0e86aec82b84437a')
uri_playlist
# %%
resultados_api = api.extraer_canciones(sp, uri_playlist)
# %%
df_canciones = api.limpiar_datos(resultados_api)
df_canciones
# %%
df_final = api.sacar_caracteristicas(df_canciones, sp)
df_final