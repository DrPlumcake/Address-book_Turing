import tkinter as tk
from tkinter import ttk


def setUp(root : tk.Tk):
    root.geometry("300x500")
    root.title("Rubrica")
    root.configure(background="#1E1E0A")
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=0, weight=1)
    root.minsize(550,300)

def setMainroot(root : tk.Tk, data):
    
    def read_data(data):
        index=0
        for index, line in enumerate(data):
            tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])
            
    
    columns = ("surname", "address", "number", "age")

    tree = ttk.Treeview(columns=columns, height=200)
    tree.grid(row=0, column=0, padx = 10, pady = 20)
    
    tree.column('#0', width=100, anchor='w')
    tree.column('surname', width=100, anchor='w')
    tree.column('address', width=100, anchor='w')
    tree.column('number', width=100, anchor='w')
    tree.column('age', width=100, anchor='w')

    tree.heading('#0', text='Name')
    tree.heading('surname', text='Surname')
    tree.heading('address', text='Address')
    tree.heading('number', text='Phone Number')
    tree.heading('age', text='Age')

    read_data(data=data)
    
    bFrame = ttk.Frame(width=300, height=100)
    bFrame.grid(row=1, column=0, sticky="S", padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    data = [
        ["Mario","Rossi", "via dei Girasoli 2", 264735917, 37],
        ["Andrea", "Fantasticini", "via dei cavoli 32", 3271871202, 23],
        ["Walter", "White", "Onegro 37", 184197491, 51],
        ["Frank", "Castle", "New York 5", 1415161631, 32],
    ]
    setUp(root=root)
    setMainroot(root=root, data=data)
    root.mainloop()
