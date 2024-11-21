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
    ttk.Button(auto_pes_root, text="Voltar", command=voltar).grid(row=5, column=0, pady=10)

def iniciar_remove_fundo():
    def voltar():
        remove_fundo_root.destroy()
        root.deiconify()

    root.withdraw()
    import RemoveFundo.RemoveFundo as RemoveFundo
    remove_fundo_root = RemoveFundo.main()
    ttk.Button(remove_fundo_root, text="Voltar", command=voltar).grid(row=5, column=0, pady=10)

def iniciar_baixar_you():
    def voltar():
        baixar_you_root.destroy()
        root.deiconify()

    root.withdraw()
    import BaixarYou.BaixarYou as BaixarYou
    baixar_you_root = BaixarYou.main()
    ttk.Button(baixar_you_root, text="Voltar", command=voltar).grid(row=5, column=0, pady=10)

def iniciar_gerenciador_tarefas():
    def voltar():
        gerenciador_tarefas_root.destroy()
        root.deiconify()

    root.withdraw()
    import GerenciadorTarefas.GerenciadorTarefas as GerenciadorTarefas
    gerenciador_tarefas_root = GerenciadorTarefas.main()
    ttk.Button(gerenciador_tarefas_root, text="Voltar", command=voltar).grid(row=5, column=0, pady=10)

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
ttk.Label(root, text="Bem-vindo ao Projeto Miski", style='TLabel').grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Botões para abrir cada projetinho
ttk.Button(root, text="Iniciar AutoPes", command=iniciar_auto_pes, style='TButton').grid(row=1, column=0, padx=10, pady=10)
ttk.Button(root, text="Iniciar RemoveFundo", command=iniciar_remove_fundo, style='TButton').grid(row=1, column=1, padx=10, pady=10)
ttk.Button(root, text="Iniciar BaixarYou", command=iniciar_baixar_you, style='TButton').grid(row=2, column=0, padx=10, pady=10)
ttk.Button(root, text="Iniciar Gerenciador de Tarefas", command=iniciar_gerenciador_tarefas, style='TButton').grid(row=2, column=1, padx=10, pady=10)

# Botão para fechar o programa
ttk.Button(root, text="Fechar Programa", command=fechar_programa, style='TButton.Red.TButton').grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
