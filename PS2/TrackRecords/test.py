import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    # Lógica para ler o arquivo JSON e salvar os dados no banco de dados

# Configuração da janela
root = tk.Tk()
root.title("Leitor JSON e Banco de Dados")

# Botão para abrir o arquivo JSON
open_button = tk.Button(root, text="Abrir Arquivo JSON", command=open_file)
open_button.pack()

# Iniciar a interface
root.mainloop()
