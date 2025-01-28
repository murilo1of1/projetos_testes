import customtkinter as ctk

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

janela = ctk.CTk()
janela.title("Conversor de Base do Bingão")
janela.geometry("400x350")

frame_1 = ctk.CTkFrame(janela, fg_color="#6f9fdb")
frame_1.pack(fill="x")

titulo = ctk.CTkLabel(frame_1, text="Conversor de Base do Bingão", font=("Comfortaa", 20), text_color="white")
titulo.pack(pady=10)

frame_2 = ctk.CTkFrame(janela)
frame_2.pack(pady=10, padx=20, fill="both", expand=True)

def conversao():
    try:
        numero = e_valor.get()
        base = combo.get()

        bases = {"BINÁRIO": 2, "OCTAL": 8, "DECIMAL": 10, "HEXADECIMAL": 16}
        decimal = int(numero, bases[base])

        binario = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:].upper()

        l_binario_valor.configure(text=binario)
        l_octal_valor.configure(text=octal)
        l_decimal_valor.configure(text=str(decimal))
        l_hexadecimal_valor.configure(text=hexadecimal)
    except:
        l_binario_valor.configure(text="Erro")
        l_octal_valor.configure(text="Erro")
        l_decimal_valor.configure(text="Erro")
        l_hexadecimal_valor.configure(text="Erro")

bases = ["BINÁRIO", "OCTAL", "DECIMAL", "HEXADECIMAL"]
combo = ctk.CTkComboBox(frame_2, values=bases, width=120)
combo.pack(pady=5)
combo.set("DECIMAL")

e_valor = ctk.CTkEntry(frame_2, width=120, justify="center")
e_valor.pack(pady=5)

b_converter = ctk.CTkButton(frame_2, text="Converter", command=conversao)
b_converter.pack(pady=10)

frame_resultados = ctk.CTkFrame(frame_2)
frame_resultados.pack(pady=5, fill="x")

def criar_linha(texto):
    frame_linha = ctk.CTkFrame(frame_resultados)
    frame_linha.pack(fill="x", pady=2)

    label = ctk.CTkLabel(frame_linha, text=texto, fg_color="#e89613",
                         text_color="white", width=120, corner_radius=8, font=("Verdana", 13))
    label.pack(side="left", padx=5)

    valor = ctk.CTkLabel(frame_linha, text="", width=150, font=("Verdana", 13), fg_color="#3b82f6",
                         text_color="white", corner_radius=8)
    valor.pack(side="right", padx=5)

    return valor

l_binario_valor = criar_linha("BINÁRIO")
l_octal_valor = criar_linha("OCTAL")
l_decimal_valor = criar_linha("DECIMAL")
l_hexadecimal_valor = criar_linha("HEXADECIMAL")

janela.mainloop()
