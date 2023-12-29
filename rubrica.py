import tkinter as tk
from tkinter import ttk


def setUp(root : tk.Tk):
    root.geometry("300x500")
    root.title("Rubrica")
    root.configure(background="#1E1E0A")
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=0, weight=1)
    root.minsize(400,300)

def setMain(root : tk.Tk, data):
    
    def read_data_to_main(data):
        index=0
        for index, line in enumerate(data):
            tree.insert('', tk.END, iid = index,
                text = line[0], values = line[1:])
    
    columns = ("surname", "number")

    tree = ttk.Treeview(columns=columns, height=200)
    tree.grid(row=0, column=0, padx = 10, pady = 20)
    
    bar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    bar.grid(row=0, column=4, sticky="ns", padx=10, pady=10)
    tree.configure(yscrollcommand=bar.set)
    
    tree.column('#0', width=120, anchor='w')
    tree.column('surname', width=120, anchor='w')
    tree.column('number', width=120, anchor='w')

    tree.heading('#0', text='Name')
    tree.heading('surname', text='Surname')
    tree.heading('number', text='Phone Number')

    read_data_to_main(data=data)

    bFrame = ttk.Frame(width=300, height=100)
    bFrame.grid(row=1, column=0, sticky="S", padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    data = [
        ["Mario","Rossi", 264735917],
        ["Andrea", "Fantasticini", 3271871202],
        ["Walter", "White", 184197491],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
        ["Frank", "Castle",  1415161631],
    ]
    setUp(root=root)
    setMain(root=root, data=data)
    root.mainloop()
