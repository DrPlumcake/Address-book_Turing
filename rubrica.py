import tkinter as tk
import mysql.connector as connector
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

class LoginWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=200)
        self.resizable(0,0)
        self.title("Login")
        
        self.user_label = ttk.Label(
            self,
            text="Enter username"
        )
        self.pass_label = ttk.Label(
            self,
            text="Enter password"
        )
        self.user_entry = ttk.Entry(
            self,
        )
        self.pass_entry = ttk.Entry(
            self,
        )
        self.Enter_Button = ttk.Button(
            self,
            text="Login",
            command= lambda: self.login_request()
        )
        
        self.user_label.grid(row=0, column=0, pady=5, padx=15, sticky="w")
        self.pass_label.grid(row=2, column=0, pady=5, padx=15, sticky="w")
        self.user_entry.grid(row=1, column=0, pady=5, padx=15, sticky="w")
        self.pass_entry.grid(row=3, column=0, pady=5, padx=15, sticky="w")
        self.Enter_Button.grid(row=4, column=0, pady=15, padx=10, sticky="s")
        
    def login_request(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        try:
            mydb = connector.connect(
                user=username,
                password=password,
            )
            
            if mydb.is_connected():
                print("Connessione a MySQL riuscita")
        except connector.Error as err:
            ErrorLoginWindow(
                self, 
                error=err
            )
        
        else:
            self.destroy()
            mainWindow= MainWindow(db=mydb)
            mainWindow.mainloop()

class ErrorWindow(tk.Toplevel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.config(width=400, height=200)
        self.resizable(0,0)

        self.label = ttk.Label(
            self,
            text="You need to select a contact to modify it or delete it"
        )
        self.label.grid(row=0, column=0, padx=10, pady=20, sticky="nwes")
        self.ok = ttk.Button(
            self,
            text="Ok",
            command=lambda:self.destroy()
        )
        self.ok.grid(row=1, column=0, padx=20, pady=5, sticky="s")
        
        self.focus()
        self.grab_set()

class ErrorLoginWindow(tk.Toplevel):
    
    def __init__(self, *args, error=None,**kwargs):
        super().__init__(*args, **kwargs)
    
        self.config(width=400, height=200)
        self.resizable(0,0)

        self.label = ttk.Label(
            self,
            text="Invalid credentials. Please check and try again."
        )
        self.label.grid(row=0, column=0, padx=10, pady=20, sticky="nwes")
        self.label_err = ttk.Label(
            self,
            text=error
        )
        self.label_err.grid(row=1, column=0, padx=10, pady=5, sticky="nwes")
        self.ok = ttk.Button(
            self,
            text="Ok",
            command=lambda:self.destroy()
        )
        self.ok.grid(row=2, column=0, padx=20, pady=5, sticky="s")
        
        self.focus()
        self.grab_set()

class CheckWindow(tk.Toplevel):
    
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.callback = callback
        self.config(width=400, height=200)
        self.resizable(0,0)
        
        self.check_label = ttk.Label(
            self,
            text="This contact will be deleted, continue?"
        )
        self.yes_Button = ttk.Button(
            self,
            text="Yes",
            command=lambda:self.delete_button()
        )
        self.no_Button = ttk.Button(
            self,
            text="No",
            command=lambda:self.destroy()
        )
        
        self.check_label.grid(row=0, column=0, pady=20, padx=10, sticky="nswe")
        self.yes_Button.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        self.no_Button.grid(row=1, column=1, pady=5, padx=10, sticky="e")
        
        self.focus()
        self.grab_set()
        
    def delete_button(self):
            self.callback()
            self.destroy()

class InputWindow(tk.Toplevel):

    def __init__(self, *args, callback=None, item : Persona | None, ind=None, **kwargs):
        super().__init__(*args, **kwargs)
        # callback is a function that this window will call
        # with the entered name as an argument once the button
        # has been pressed.
        self.callback = callback
        self.config(width=400, height=400)
        # Disable the button for resizing the window.
        self.resizable(0, 0)
        self.title("Insert Contact Info")
        
        modify= False
        if item != None:
            modify= True
        
        # Insert Name Info
        self.labelName = ttk.Label(
            self,
            text="Insert Name"
        )
        self.labelName.grid(row=0, column=0, sticky="w", padx=10, pady=2)
        self.entry_name = ttk.Entry(self)
        self.entry_name.grid(row=1, column=0, sticky="w", padx=10, pady=2)
        if modify:
            self.entry_name.insert(index=0, string=item.name)
        
        # Insert Surname
        self.labelSurname = ttk.Label(
            self,
            text="Insert Surname"
        )
        self.labelSurname.grid(row=2, column=0, sticky="w", padx=10, pady=2)
        self.entry_surname = ttk.Entry(self)
        self.entry_surname.grid(row=3, column=0, sticky="w", padx=10, pady=2)
        if modify:
            self.entry_surname.insert(index=0, string=item.surname)
        
        # Insert Number
        self.labelNumber = ttk.Label(
            self,
            text="Insert Number"
        )
        self.labelNumber.grid(row=4, column=0, sticky="w", padx=10, pady=2)
        self.entry_number = ttk.Entry(self)
        self.entry_number.grid(row=5, column=0, sticky="w", padx=10, pady=2)
        if modify:
            self.entry_number.insert(index=0, string=item.number)
        
        # Insert Address
        self.labelAddress = ttk.Label(
            self,
            text="Insert Address"
        )
        self.labelAddress.grid(row=6, column=0, sticky="w", padx=10, pady=2)
        self.entry_address = ttk.Entry(self)
        self.entry_address.grid(row=7, column=0, sticky="w", padx=10, pady=2)
        if modify:
            self.entry_address.insert(index=0, string=item.address)
        
        # Insert Age
        self.labelAge = ttk.Label(
            self,
            text="Insert Age"
        )
        self.labelAge.grid(row=8, column=0, sticky="w", padx=10, pady=2)
        self.entry_age = ttk.Entry(self)
        self.entry_age.grid(row=9, column=0, sticky="w ", padx=10, pady=2)
        if modify:
            self.entry_age.insert(index=0, string=str(item.age))
        
        #Button Done
        self.button_done = ttk.Button(
            self,
            text="Submit",
            command= lambda: self.Save(mod=modify, item=item, ind=ind)
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

    def Save(self, mod, item, ind):
        # Get the entered name and invoke the callback function
        # passed when creating this window.
        if mod:
            new_p = item
            new_p.name=self.entry_name.get(),
            new_p.surname=self.entry_surname.get(),
            new_p.address = self.entry_address.get(),
            new_p.address = new_p.address[0]
            new_p.number=self.entry_number.get(),
            new_p.age=self.entry_age.get()
            self.callback(person=new_p, index=ind)
        
        else: 
            new_p = Persona(
                name=self.entry_name.get(),
                surname=self.entry_surname.get(),
                address=self.entry_address.get(),
                number=self.entry_number.get(),
                age=self.entry_age.get()
                )
            data.append(new_p)
            self.callback(person=new_p)
        
        # Close the window.
        self.destroy()

class MainWindow(tk.Tk):

    def __init__(self, *args, db=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300, background="white")
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
        self.button_new = ttk.Button(
            bFrame,
            text="New Contact",
            command=lambda: self.new_contact()
        )
        self.button_modify = ttk.Button(
            bFrame,
            text="Modify Contact",
            command=lambda: self.modify_contact()
        )
        self.button_delete = ttk.Button(
            bFrame,
            text="Delete Contact",
            command=lambda: self.delete_request()
        )
        self.button_new.grid(row=1, column=0)
        self.button_modify.grid(row=1, column=1)
        self.button_delete.grid(row=1, column=2)

    def new_contact(self):
        # Create the child window and pass the callback
        # function 
        
        self.New_window = InputWindow(
            callback=self.new_contact_save,
            item=None,
            ind=None
        )

    def new_contact_save(self, person : Persona):
        # This function is invoked once the user presses the
        # "Submit" button within the secondary window. 
        
        self.tree.insert('', tk.END,
            text = person.name, values = [person.surname, person.number])
        
    def modify_contact(self):
        # row index
        item = self.tree.focus()
        if item == "":
            self.error = ErrorWindow()
            return
        p = data[int(item)]
        
        self.New_window = InputWindow(
            callback=self.update_contact,
            item=p,
            ind=item
        )
        
    def update_contact(self, person : Persona, index):
        # Save data
        self.tree.item(index, text=person.name, values=[person.surname, person.number])

    def delete_request(self):
        
        item = self.tree.focus()
        if item == "":
            self.error = ErrorWindow()
            return
        
        self.Check_Window = CheckWindow(
            callback=self.delete_contact,
        )
        
    def delete_contact(self):
        
        self.tree.delete(self.tree.focus())
       
if __name__ == "__main__":
    
    login_window = LoginWindow()
    login_window.mainloop()