from doctest import master
from tkinter import ttk, StringVar, constants

class LoginView:
    def __init__(self, root, handlelogin, handlecreateuserview):
        self._root=root
        self._handle_login=handlelogin
        self._handle_createuser_view=handlecreateuserview
        self._frame=None
        self._username_entry=None
        self._password_entry=None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)
    
    def destroy(self):
        self.frame.destroy()

    def _login_handler(self):
        username=self.username_entry.get()
        password=self.password_entry.get()

    def _initialize_username_area(self):
        username_text=ttk.Label(master=self._frame, text='Username')
        self._username_entry=ttk.Entry(master=self._frame)

        username_text.grid(padx=10, pady=10, sticky=constants.W)
        self._username_entry.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize_password_area(self):
        password_text=ttk.Label(master=self, text='Password')
        self._password_entry=ttk.Entry(master=self._frame)

        password_text.grid(padx=10, pady=10, sticky=constants.W)
        self._password_entry.grid(padx=10, pady=10, sticky=constants.EW)