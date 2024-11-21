import tkinter as tk
from tkinter import ttk

# Funções principais para iniciar cada projetinho
def iniciar_auto_pes():
    def voltar():
        auto_pes_root.destroy()
        root.deiconify()

    root.withdraw()
    import AutoPes.AutoPes as AutoPes
    auto_pes_root = AutoPes.main()
    voltar_button = ttk.Button(auto_pes_root, text="Voltar", command=voltar)
    voltar_button.pack(pady=10)

def iniciar_remove_fundo():
    def voltar():
        remove_fundo_root.destroy()
        root.deiconify()

    root.withdraw()
    import RemoveFundo.RemoveFundo as RemoveFundo
    remove_fundo_root = RemoveFundo.main()
    voltar_button = ttk.Button(remove_fundo_root, text="Voltar", command=voltar)
    voltar_button.pack(pady=10)

def iniciar_baixar_you():
    def voltar():
        baixar_you_root.destroy()
        root.deiconify()

    root.withdraw()
    import BaixarYou.BaixarYou as BaixarYou
    baixar_you_root = BaixarYou.main()
    voltar_button = ttk.Button(baixar_you_root, text="Voltar", command=voltar)
    voltar_button.pack(pady=10)

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
