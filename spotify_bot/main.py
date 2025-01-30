import customtkinter as ctk
from spotify_api import buscar_musica, criar_playlist, adicionar_musica_playlist, verificar_musicas_mais_tocadas

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Spotify Bot")
app.geometry("550x500")

def buscar():
    nome_musica = entrada_musica.get()
    resultado = buscar_musica(nome_musica)
    output_label.configure(text=resultado)

def criar():
    nome_playlist = entrada_playlist.get()
    resultado = criar_playlist(nome_playlist)
    output_label.configure(text=resultado)

def adicionar():
    playlist_id = entrada_playlist_id.get()
    nome_musica = entrada_musica.get()
    resultado = adicionar_musica_playlist(playlist_id, nome_musica)
    output_label.configure(text=resultado)

def mostrar_top_musicas():
    resultado = verificar_musicas_mais_tocadas()
    output_label.configure(text=resultado, anchor="w", justify="left")

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="both", expand=True)

titulo = ctk.CTkLabel(frame, text="🎵 Spotify Bot", font=("Arial", 22, "bold"))
titulo.pack(pady=10)

entrada_musica = ctk.CTkEntry(frame, placeholder_text="Digite o nome da música")
entrada_musica.pack(pady=5, fill="x", padx=20)

btn_buscar = ctk.CTkButton(frame, text="🔍 Buscar Música", command=buscar)
btn_buscar.pack(pady=5)

entrada_playlist = ctk.CTkEntry(frame, placeholder_text="Nome da Playlist")
entrada_playlist.pack(pady=5, fill="x", padx=20)

btn_criar = ctk.CTkButton(frame, text="➕ Criar Playlist", command=criar)
btn_criar.pack(pady=5)

entrada_playlist_id = ctk.CTkEntry(frame, placeholder_text="ID da Playlist")
entrada_playlist_id.pack(pady=5, fill="x", padx=20)

btn_adicionar = ctk.CTkButton(frame, text="🎶 Adicionar Música à Playlist", command=adicionar)
btn_adicionar.pack(pady=5)

btn_top_musicas = ctk.CTkButton(frame, text="🔥 Músicas Mais Tocadas", command=mostrar_top_musicas)
btn_top_musicas.pack(pady=5)

output_label = ctk.CTkLabel(frame, text="", wraplength=450, font=("Arial", 14), justify="left", anchor="w")
output_label.pack(pady=10, padx=20)

app.mainloop()
