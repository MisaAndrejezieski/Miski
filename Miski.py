import tkinter as tk
from tkinter import ttk

# Funções principais para iniciar cada projetinho
def iniciar_auto_pes():
    import AutoPes.AutoPes as AutoPes
    AutoPes.main()

def iniciar_remove_fundo():
    import RemoveFundo.RemoveFundo as RemoveFundo
    RemoveFundo.main()

def iniciar_baixar_you():
    import BaixarYou.BaixarYou as BaixarYou
    BaixarYou.main()

# Função para fechar o programa
def fechar_programa():
    root.quit()

# Configuração da interface gráfica principal
root = tk.Tk()
root.title("Miski - Projeto Principal")
root.geometry('600x400')
root.configure(bg='#282c34')

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton', background='#4CAF50', foreground='#ffffff', font=('Helvetica', 12, 'bold'))
style.map('TButton', background=[('active', '#56b6c2')])
style.configure('TButton.Red.TButton', background='#f44336', foreground='#ffffff', font=('Helvetica', 12, 'bold'))
style.map('TButton.Red.TButton', background=[('active', '#d32f2f')])
style.configure('TLabel', background='#282c34', foreground='#61afef', font=('Helvetica', 10))
style.configure('TEntry', font=('Helvetica', 10))

# Elementos da interface principal
ttk.Label(root, text="Bem-vindo ao Projeto Miski", style='TLabel').pack(pady=20)

# Botões para abrir cada projetinho
ttk.Button(root, text="Iniciar AutoPes", command=iniciar_auto_pes, style='TButton').pack(pady=10)
ttk.Button(root, text="Iniciar RemoveFundo", command=iniciar_remove_fundo, style='TButton').pack(pady=10)
ttk.Button(root, text="Iniciar BaixarYou", command=iniciar_baixar_you, style='TButton').pack(pady=10)

# Botão para fechar o programa
ttk.Button(root, text="Fechar Programa", command=fechar_programa, style='TButton.Red.TButton').pack(pady=20)

root.mainloop()
