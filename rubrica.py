import tkinter as tk
from tkinter import ttk

class Persona():
    
    def __init__(self, name : str, surname : str, address : str, number : str, age : int):
        self.name = name
        self.surname = surname
        self.address = address
        self.number = number
        self.age = age
        
    def setName(self, name):
        self.name = name
        
    def setSurname(self, surname):
        self.surname = surname
    
    def setAddress(self, address):
        self.address = address
        
    def setNumber(self, number):
        self.number = number
        
    def setAge(self, age):
        self.age = age
        
data = [
    Persona("Mario", "Rossi", "Casa 1", "2384123512", 34),
    Persona("Andrea", "Fantasticini", "Casa 2", "2349374902", 23),
    Persona("Frank", "Castle", "Casa 3", "32415161613", 37),
    ]

class InputWindow(tk.Toplevel):

    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        # callback is a function that this window will call
        # with the entered name as an argument once the button
        # has been pressed.
        self.callback = callback
        self.config(width=400, height=400)
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
            command= lambda: self.Save()
        )
        self.button_done.grid(row=10, column=0, sticky="w", padx=10, pady=20)
        
        #Button Cancel
        self.button_cancel = ttk.Button(
            self,
            text="Cancel",
            command= lambda: self.destroy()
        )
        self.button_cancel.grid(row=10, column=1, sticky="e", padx=10, pady=20)
        
        self.focus()
        self.grab_set()

    def Save(self):
        # Get the entered name and invoke the callback function
        # passed when creating this window.
        
        new_p = Persona(
            name=self.entry_name.get(),
            surname=self.entry_surname.get(),
            address=self.entry_address.get(),
            number=self.entry_number.get(),
            age=self.entry_age.get()
            )
        
        data.append(new_p)
        
        self.callback(new_p)
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
        
        def read_data_to_main(data):
            index=0
            for index, person in enumerate(data):
                self.tree.insert('', tk.END, iid = index,
                    text = person.name, values = [person.surname, person.number])
        
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
        
        self.label_error = ttk.Label(
            bFrame,
            text="You need to select a contact to modify it"
        )
        self.button_new = ttk.Button(
            bFrame,
            text="New Contact",
            command=lambda: self.new_contact()
        )
        self.button_modify = ttk.Button(
            bFrame,
            text="Modify Contact",
        )
        self.button_delete = ttk.Button(
            bFrame,
            text="Delete Contact",
        )
        self.button_new.grid(row=1, column=0)
        self.button_modify.grid(row=1, column=1)
        self.button_delete.grid(row=1, column=2)

    def new_contact(self):
        # Create the child window and pass the callback
        # function by which we want to receive the entered
        # name.
        self.New_window = InputWindow(
            callback=self.new_contact_save
        )

    def new_contact_save(self, person : Persona):
        # This function is invoked once the user presses the
        # "Submit" button within the secondary window. 
        
        self.tree.insert('', tk.END,
            text = person.name, values = [person.surname, person.number])

if __name__ == "__main__":
    
    main_window = MainWindow()
    main_window.mainloop()