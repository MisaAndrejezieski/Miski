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
    if input_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, input_path)

# Função para procurar o arquivo de saída
def browse_output():
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if output_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, output_path)

# Função para iniciar o processo
def start_process():
    input_path = entry_input.get()
    output_path = entry_output.get()
    if not input_path or not output_path:
        messagebox.showwarning("Atenção", "Por favor, selecione os arquivos de entrada e saída.")
        return
    message = process_image(input_path, output_path)
    messagebox.showinfo("Resultado", message)

# Criar a interface gráfica
app = tk.Tk()
app.title("Remove Fundo de Imagem")
app.configure(bg='#0000ff')  # Configura o fundo em tom azul

# Estilos dos widgets
bg_color = '#ff3399'          # Rosa para os rótulos
fg_color = '#333'             # Cor do texto
button_color = '#add8e6'      # Azul claro para os botões
entry_bg_color = '#fff'       # Branco para o fundo das entradas
entry_fg_color = '#333'       # Cor do texto das entradas

# Elementos da interface
tk.Label(app, text="Arquivo de entrada:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=10)
entry_input = tk.Entry(app, width=50, bg=entry_bg_color, fg=entry_fg_color)
entry_input.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Procurar", command=browse_input, bg=button_color, fg=fg_color).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Arquivo de saída:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=10)
entry_output = tk.Entry(app, width=50, bg=entry_bg_color, fg=entry_fg_color)
entry_output.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Salvar como", command=browse_output, bg=button_color, fg=fg_color).grid(row=1, column=2, padx=10, pady=10)

tk.Button(app, text="Iniciar", command=start_process, bg=button_color, fg=fg_color).grid(row=2, column=1, pady=20)

# Iniciar a interface gráfica
app.mainloop()
