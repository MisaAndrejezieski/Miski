import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
from datetime import datetime

# Caminho do arquivo de tarefas
tasks_file = os.path.join(os.path.dirname(__file__), 'tasks.json')

# Função para carregar as tarefas
def load_tasks():
    if os.path.isfile(tasks_file):
        with open(tasks_file, 'r') as file:
            return json.load(file)
    return []

# Função para salvar as tarefas
def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)

# Função para adicionar uma nova tarefa
def add_task():
    task = entry_task.get()
    due_date = entry_date.get()
    if not task or not due_date:
        messagebox.showwarning("Atenção", "Por favor, preencha todas as informações.")
        return

    try:
        datetime.strptime(due_date, '%d/%m/%Y %H:%M')
    except ValueError:
        messagebox.showwarning("Atenção", "Data e hora no formato incorreto. Use DD/MM/AAAA HH:MM.")
        return

    tasks.append({'task': task, 'due_date': due_date, 'done': False})
    save_tasks(tasks)
    update_task_list()
    entry_task.delete(0, tk.END)
    entry_date.delete(0, tk.END)

# Função para atualizar a lista de tarefas
def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "Concluída" if task['done'] else "Pendente"
        listbox_tasks.insert(tk.END, f"{task['task']} - {task['due_date']} - {status}")

# Função para marcar uma tarefa como concluída
def complete_task():
    selected_task = listbox_tasks.curselection()
    if not selected_task:
        messagebox.showwarning("Atenção", "Por favor, selecione uma tarefa.")
        return
    
    index = selected_task[0]
    tasks[index]['done'] = True
    save_tasks(tasks)
    update_task_list()

# Função para excluir uma tarefa
def delete_task():
    selected_task = listbox_tasks.curselection()
    if not selected_task:
        messagebox.showwarning("Atenção", "Por favor, selecione uma tarefa.")
        return

    index = selected_task[0]
    tasks.pop(index)
    save_tasks(tasks)
    update_task_list()

# Função principal para iniciar a interface gráfica
def main():
    global entry_task, entry_date, listbox_tasks, tasks

    tasks = load_tasks()
    
    root = tk.Tk()
    root.title("Gerenciador de Tarefas")
    root.geometry('600x400')
    root.configure(bg='#cfffca')

    # Estilos dos widgets
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', background='#A7D8D7', foreground='#2E4053', font=('Helvetica', 12, 'bold'))
    style.map('TButton', background=[('active', '#80C7C6')])
    style.configure('Red.TButton', background='#F28C8C', foreground='#2E4053', font=('Helvetica', 12, 'bold'))
    style.map('Red.TButton', background=[('active', '#F76C6C')])
    style.configure('TLabel', background='#F3F4F6', foreground='#2E4053', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12), padding=5)

    # Elementos da interface
    ttk.Label(root, text="Tarefa:", style='TLabel').grid(row=0, column=0, padx=10, pady=10)
    entry_task = ttk.Entry(root, width=50)
    entry_task.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="Data e Hora (DD/MM/AAAA HH:MM):", style='TLabel').grid(row=1, column=0, padx=10, pady=10)
    entry_date = ttk.Entry(root, width=50)
    entry_date.grid(row=1, column=1, padx=10, pady=10)

    add_button = ttk.Button(root, text="Adicionar Tarefa", command=add_task, style='TButton')
    add_button.grid(row=2, column=1, pady=10)

    listbox_tasks = tk.Listbox(root, width=70, height=10)
    listbox_tasks.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    complete_button = ttk.Button(root, text="Marcar como Concluída", command=complete_task, style='TButton')
    complete_button.grid(row=4, column=0, pady=10)

    delete_button = ttk.Button(root, text="Excluir Tarefa", command=delete_task, style='Red.TButton')
    delete_button.grid(row=4, column=1, pady=10)

    update_task_list()

    # Iniciar a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
