from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Função para processar a imagem
def process_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        output = remove(img)
        output.save(output_path)
        return "Imagem processada e salva com sucesso!"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Função para procurar o arquivo de entrada
def browse_input():
    input_path = filedialog.askopenfilename()
