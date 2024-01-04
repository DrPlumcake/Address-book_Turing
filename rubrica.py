import tkinter as tk
import mysql.connector as connector
from tkinter import ttk
import pathlib

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

# Used when there is not a properties file
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
        # Inser Username
        self.user_entry = ttk.Entry(
            self,
        )
        # Insert Password (Secure)
        self.pass_entry = ttk.Entry(
            self,
            show="*"
        )
        # Enter Credentials Button
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
        
    # Login Request and connection to DB
    def login_request(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        try:
            mydb = connector.connect(
                user=username,
                password=password,
                database="rubrica_schema"
            )
        except connector.Error as err:
            ErrorLoginWindow(
                self, 
                error=err
            )
        # Connection succeded
        else:
            self.destroy()
            mainWindow= MainWindow(db=mydb)
            mainWindow.mainloop()

# Pop Up Error Window for Modify and Delete Operations
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
        
        # No interaction with the main Window
        self.focus()
        self.grab_set()

# Pop Up Error Window for Login Operation
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
        
        # No interaction with the main Window
        self.focus()
        self.grab_set()

# Check Window for Delete Operations
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
        # Delete Operation Confirmed
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
        
        # No interaction with the main Window
        self.focus()
        self.grab_set()
        
    # Cancel Delete Operation
    def delete_button(self):
            self.callback()
            self.destroy()

# Editor Window for Modify and Create Operations
class InputWindow(tk.Toplevel):

    def __init__(self, *args, callback=None, item : Persona | None, key=None, **kwargs):
        super().__init__(*args, **kwargs)
        # callback is a function that this window will call
        # with the entered data as an argument once the button
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
            command= lambda: self.Save(mod=modify, item=item, key=key)
        )
        self.button_done.grid(row=10, column=0, sticky="w", padx=10, pady=20)
        
        #Button Cancel
        self.button_cancel = ttk.Button(
            self,
            text="Cancel",
            command= lambda: self.destroy()
        )
        self.button_cancel.grid(row=10, column=1, sticky="e", padx=10, pady=20)
        
        # No interaction with the main Window
        self.focus()
        self.grab_set()

    def Save(self, mod, item, key):
        # Get the entered data and invoke the callback function
        # passed when creating this window.
        if mod:
            new_p = item
            new_p.name=self.entry_name.get(),
            new_p.surname=self.entry_surname.get(),
            new_p.address = self.entry_address.get(),
            new_p.number=self.entry_number.get(),
            new_p.age=self.entry_age.get()
            # Modify Entry to DB
            self.callback(person=new_p, key=key)
        
        else: 
            new_p = Persona(
                name=self.entry_name.get(),
                surname=self.entry_surname.get(),
                address=self.entry_address.get(),
                number=self.entry_number.get(),
                age=self.entry_age.get()
                )
            # Add Entry to DB
            self.callback(person=new_p)
        
        # Close the window.
        self.destroy()

# Main Window of 'Rubrica'
class MainWindow(tk.Tk):

    def __init__(self, db : connector.MySQLConnection, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Config of the window
        self.config(width=400, height=300, background="white")
        self.minsize(400,300)
        self.geometry("400x300")
        self.title("Rubrica")
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)
        
        # Frame for the Buttons
        bFrame = ttk.Frame(width=300, height=100)
        bFrame.grid(row=1, column=0, sticky="S", padx=10, pady=10)
        
        # DB cursor
        self.datab = db
        self.cursor = self.datab.cursor()
        
        # Treeview
        columns = ("surname", "number")
        self.tree = ttk.Treeview(columns=columns, height=200)
        self.tree.grid(row=0, column=0, padx = 10, pady = 20)
        
        # Scrollbar
        self.bar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.bar.grid(row=0, column=4, sticky="ns", padx=10, pady=10)
        self.tree.configure(yscrollcommand=self.bar.set)
        
        # Treeview config
        self.tree.column('#0', width=100, anchor='w')
        self.tree.column('surname', width=100, anchor='w')
        self.tree.column('number', width=100, anchor='w')

        self.tree.heading('#0', text='Name')
        self.tree.heading('surname', text='Surname')
        self.tree.heading('number', text='Phone Number')
        
        self.refresh()
        
        # New Contact Button
        self.button_new = ttk.Button(
            bFrame,
            text="New Contact",
            command=lambda: self.new_contact()
        )
        # Modify Contact Button
        self.button_modify = ttk.Button(
            bFrame,
            text="Modify Contact",
            command=lambda: self.modify_contact()
        )
        # Delete Contact Button
        self.button_delete = ttk.Button(
            bFrame,
            text="Delete Contact",
            command=lambda: self.delete_request()
        )
        self.button_new.grid(row=1, column=0)
        self.button_modify.grid(row=1, column=1)
        self.button_delete.grid(row=1, column=2)

    # Refresh Treeview function
    def refresh(self):
        if self.datab.is_connected():
            query = "SELECT * FROM Contatti"
            self.cursor.execute(query)
            
            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in self.cursor.fetchall():
                self.tree.insert('', tk.END, text=row[0], values=[row[1], row[2]])
    
    def new_contact(self):
        # Create the child window and pass the callback
        # function 
        self.New_window = InputWindow(
            callback=self.new_contact_save,
            item=None,
        )

    def new_contact_save(self, person : Persona):
        # This function is invoked once the user presses the
        # "Submit" button within the secondary window. 
        query = "INSERT INTO Contatti VALUES (%s, %s, %s, %s, %s)"
        params = (
            person.name,
            person.surname,
            person.number,
            person.address,
            str(person.age)
        )
        
        self.cursor.execute(query, params)
        
        # Apply changes to table
        self.datab.commit()
        
        self.refresh()
        
    def modify_contact(self):
        # row index
        item = self.tree.focus()
        if item == "":
            self.error = ErrorWindow()
            return
        
        values = self.tree.item(item, 'values')
        key = values[1]
        
        # 'Numero' is a Primary key
        query = f"SELECT * FROM Contatti WHERE Numero = {key}"
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        
        p = Persona(
            name=row[0],
            surname=row[1],
            number=row[2],
            address=row[3],
            age=row[4]
        )
        
        # Editor
        self.New_window = InputWindow(
            callback=self.update_contact,
            item=p,
            key=key
        )
        
    def update_contact(self, person : Persona, key):
        # Save data to DB
        query = ("UPDATE Contatti "
            "SET Nome = %(name)s, Cognome = %(surname)s, Numero = %(number)s, "
            "Indirizzo = %(address)s, Eta = %(age)s "
            "WHERE Numero = %(key)s")
        params = {
            "name": person.name[0],
            "surname": person.surname[0],
            "number": person.number[0],
            "address": person.address[0],
            "age": str(person.age),
            "key": key
        }
        self.cursor.execute(query, params)
        
        # Apply changes to table
        self.datab.commit()
        
        self.refresh()
        

    def delete_request(self):
        # Start Delete Operation
        item = self.tree.focus()
        if item == "":
            self.error = ErrorWindow()
            return
        
        self.Check_Window = CheckWindow(
            callback=self.delete_contact,
        )
        
    def delete_contact(self):
        # Completing Delete Operation
        item = self.tree.focus()
        values = self.tree.item(item, 'values')
        key = values[1]
        query = f"DELETE FROM Contatti WHERE Numero = {key}"
        self.cursor.execute(query)
        
        # Apply changes to table
        self.datab.commit()
        
        self.refresh()
       
if __name__ == "__main__":
    
    # Searching for credientals
    DIR = pathlib.Path(__file__).parent
    CREDFILE= DIR / "credentials_database.properties"
    if CREDFILE.exists():
        with open(CREDFILE) as file:
            credentials = file.readlines()
            print(credentials)
        try:
            mydb = connector.connect(
                user=credentials[0][5:].strip(),
                password=credentials[1][9:].strip(),
                host=credentials[2][5:].strip(),
                database=credentials[3][7:].strip(),
                port=credentials[4][5:]
            )
        except connector.Error as err:
            print(err)
            login_window = LoginWindow()
            login_window.mainloop()
        else:
            mainWindow= MainWindow(db=mydb)
            mainWindow.mainloop()
    
    # No credentials file -> Login Window
    else:
        login_window = LoginWindow()
        login_window.mainloop()