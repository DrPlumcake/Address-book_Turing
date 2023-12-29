import tkinter as tk
from tkinter import ttk


class InputWindow(tk.Toplevel):

    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        # callback is a function that this window will call
        # with the entered name as an argument once the button
        # has been pressed.
        self.callback = callback
        self.config(width=300, height=400)
        # Disable the button for resizing the window.
        self.resizable(0, 0)
        self.title("Insert Contact Info")
        
        # Insert Name Info
        self.labelName = ttk.Label(
            self,
            text="Insert Name"
        )
        self.labelName.grid(row=0, column=0, sticky="w", padx=10, pady=2)
        self.entry_name = ttk.Entry(self)
        self.entry_name.grid(row=1, column=0, sticky="w", padx=10, pady=2)
        
        # Insert Surname
        self.labelSurname = ttk.Label(
            self,
            text="Insert Surname"
        )
        self.labelSurname.grid(row=2, column=0, sticky="w", padx=10, pady=2)
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.grid(row=3, column=0, sticky="w", padx=10, pady=2)
        
        # Insert Number
        self.labelNumber = ttk.Label(
            self,
            text="Insert Number"
        )
        self.labelNumber.grid(row=4, column=0, sticky="w", padx=10, pady=2)
        self.entry_number = ttk.Entry(self)
        self.entry_number.grid(row=5, column=0, sticky="w", padx=10, pady=2)
        
        # Insert Address
        self.labelAddress = ttk.Label(
            self,
            text="Insert Address"
        )
        self.labelAddress.grid(row=6, column=0, sticky="w", padx=10, pady=2)
        self.entry_address = ttk.Entry(self)
        self.entry_address.grid(row=7, column=0, sticky="w", padx=10, pady=2)
        
        # Insert Age
        self.labelAge = ttk.Label(
            self,
            text="Insert Age"
        )
        self.labelAge.grid(row=8, column=0, sticky="w", padx=10, pady=2)
        self.entry_age = ttk.Entry(self)
        self.entry_age.grid(row=9, column=0, sticky="w", padx=10, pady=2)
        
        #Button Done
        self.button_done = ttk.Button(
            self,
            text="Submit",
            command=self.button_done_pressed
        )
        self.button_done.grid(row=10, column=0, sticky="w", padx=10, pady=20)
        
        #Button Cancel
        self.button_cancel = ttk.Button(
            self,
            text="Cancel",
            command=self.button_done_pressed
        )
        self.button_cancel.grid(row=10, column=1, sticky="e", padx=10, pady=20)
        
        self.focus()
        self.grab_set()

    def button_done_pressed(self):
        # Get the entered name and invoke the callback function
        # passed when creating this window.
        self.callback(self.entry_name.get())
        # Close the window.
        self.destroy()


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300, background="#1E1E0A")
        self.minsize(400,300)
        self.geometry("400x300")
        self.title("Rubrica")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        
        bFrame = ttk.Frame(width=300, height=100)
        bFrame.grid(row=1, column=0, sticky="S", padx=10, pady=10)
        self.button_new = ttk.Button(
            bFrame,
            text="New Contact",
            command=self.request_name
        )
        self.button_modify = ttk.Button(
            bFrame,
            text="Modify Contact",
        )
        self.button_delete = ttk.Button(
            bFrame,
            text="Delete Contact",
        )
        self.label_name = ttk.Label(
            bFrame,
            text="You have not entered your name yet."
        )
        self.button_new.grid(row=1, column=0)
        self.button_modify.grid(row=1, column=1)
        self.button_delete.grid(row=1, column=2)
        
        def read_data_to_main(data):
            index=0
            for index, line in enumerate(data):
                self.tree.insert('', tk.END, iid = index,
                    text = line[0], values = line[1:])
        
        columns = ("surname", "number")

        self.tree = ttk.Treeview(columns=columns, height=200)
        self.tree.grid(row=0, column=0, padx = 10, pady = 20)
        
        self.bar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.bar.grid(row=0, column=4, sticky="ns", padx=10, pady=10)
        self.tree.configure(yscrollcommand=self.bar.set)
        
        self.tree.column('#0', width=120, anchor='w')
        self.tree.column('surname', width=120, anchor='w')
        self.tree.column('number', width=120, anchor='w')

        self.tree.heading('#0', text='Name')
        self.tree.heading('surname', text='Surname')
        self.tree.heading('number', text='Phone Number')

        read_data_to_main(data=data)

    def request_name(self):
        # Create the child window and pass the callback
        # function by which we want to receive the entered
        # name.
        self.ventana_nombre = InputWindow(
            callback=self.name_entered
        )

    def name_entered(self, name):
        # This function is invoked once the user presses the
        # "Submit" button within the secondary window. The entered
        # name will be in the "name" argument.
        self.label_name.config(
            text="Your name is: " + name
        )

if __name__ == "__main__":
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
    main_window = MainWindow()
    main_window.mainloop()