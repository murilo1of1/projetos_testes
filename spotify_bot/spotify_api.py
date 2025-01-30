import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = config.SPOTIPY_CLIENT_ID,
    client_secret = config.SPOTIPY_CLIENT_SECRET,
    redirect_uri = config.SPOTIPY_REDIRECT_URI,
    scope = "user-library-read playlist-modify-public user-top-read"
))

def buscar_musica(nome):
    resultado = sp.search(q=nome, limit=1)
    if resultado["tracks"]["items"]:
        musica = resultado["tracks"]["items"][0]
        nome = musica["name"]
        artista = musica["artists"][0]["name"]
        link = musica["external_urls"]["spotify"]
        return f"🎵{nome} - {artista}\n🔗 {link}" 
    else:
        return "Música não encontrada!"
    
def criar_playlist(name, descricao = "Criada pelo bot!"):
    usuario = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=usuario, name=name, public=True, description=descricao)
    return f"✅ Playlist criada: {playlist['external_urls']['spotify']}"
    
def adicionar_musica_playlist(playlist_id, nome_musica):
    resultado = sp.search(q=nome_musica, limit=1)
    if resultado.get("tracks") and resultado["tracks"].get("items"):
        track_id = resultado["tracks"]["items"][0]["id"]
        sp.playlist_add_items(playlist_id, [track_id])
        return f"🎶 {nome_musica} foi adicionada à playlist!"
    else:
        return "❌ Música não encontrada!"
    
def verificar_musicas_mais_tocadas(periodo="medium_term"):
    top_tracks = sp.current_user_top_tracks(limit=5, time_range=periodo)
    if not top_tracks["items"]:
        return "❌ Nenhuma música foi encontrada no seu histórico."
    resultado = "🔥 Músicas mais tocadas:\n\n"
    for track in top_tracks["items"]:
        nome = track["name"]
        artista = track["artists"][0]["name"]
        resultado += f"🎵 {nome} - {artista}\n"
    return resultado  

