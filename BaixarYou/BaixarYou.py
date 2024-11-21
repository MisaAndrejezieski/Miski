import yt_dlp
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Função para download do vídeo
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'Unknown')
            thumbnail_url = info_dict.get('thumbnail', 'No thumbnail available')
        return title, thumbnail_url
    except Exception as e:
        return None, str(e)

# Função para iniciar o download
def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL.")
        return
    progress_label.config(text="Iniciando download...")
    root.update_idletasks()
    title, result = download_video(url)
    if title:
        progress_label.config(text="Download concluído!")
        messagebox.showinfo("Sucesso", f"Título: {title}\nMiniatura: {result}")
    else:
        progress_label.config(text="Erro no download.")
        messagebox.showerror("Erro", f"Ocorreu um erro: {result}")

# Função para fechar o programa
def close_program():
    root.quit()

# Função principal
def main():
    root = tk.Tk()
    root.title("Downloader de Vídeos")

    # Defina o caminho completo do ícone
    icon_path = 'D:\\BaixarYou\\Letter-B-icon_34764.ico'
    root.iconbitmap(icon_path)

    # Configuração de cores e estilos
    root.geometry('500x300')
    root.configure(bg='#282c34')

    style = ttk.Style()
    style.theme_use('clam')

    style.configure('TButton', background='#4CAF50', foreground='#ffffff', font=('Helvetica', 12, 'bold'))
    style.map('TButton', background=[('active', '#56b6c2')])
    style.configure('TButton.Red.TButton', background='#f44336', foreground='#ffffff', font=('Helvetica', 12, 'bold'))
    style.map('TButton.Red.TButton', background=[('active', '#d32f2f')])
    style.configure('TLabel', background='#282c34', foreground='#61afef', font=('Helvetica', 10))
    style.configure('TEntry', font=('Helvetica', 10))

    # Elementos da interface
    ttk.Label(root, text="Cole aqui sua URL:", style='TLabel').pack(pady=20)
    global url_entry
    url_entry = ttk.Entry(root, width=50)
    url_entry.pack(pady=5)

    start_button = ttk.Button(root, text="Iniciar Download", command=start_download, style='TButton')
    start_button.pack(pady=20)

    close_button = ttk.Button(root, text="Fechar Programa", command=close_program, style='TButton.Red.TButton')
    close_button.pack(pady=10)

    global progress_label
    progress_label = ttk.Label(root, text="", style='TLabel')
    progress_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
