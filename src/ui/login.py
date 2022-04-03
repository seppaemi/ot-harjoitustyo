from tkinter import Tk, ttk, constants,StringVar
import matplotlib
matplotlib.use('Agg')

window = Tk()

class LoginView:
    def __init__(self, root, handlelogin, handlenewuserview):
        self._root=root
        self._handle_login=handlelogin
        self._handle_new_user_view=handlenewuserview
        self._frame=None
        self._username_entry=None
        self._password_entry=None
        self._error_variable=None
        self._error_text=None

        self._initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)
    
    def destroy(self):
        self.frame.destroy()

    def _login_handler(self):
        username=self._username_entry.get()
        password=self._password_entry.get()

    def _initialize_username_area(self):
        username_text=ttk.Label(master=self._frame, text='Username', foreground='white', background='black')
        self._username_entry=ttk.Entry(master=self._frame)

        username_text.grid(padx=10, pady=10, sticky=constants.W)
        self._username_entry.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize_password_area(self):
        password_text=ttk.Label(master=self, text='Password', foreground='white', background='black')
        self._password_entry=ttk.Entry(master=self._frame)

        password_text.grid(padx=10, pady=10, sticky=constants.W)
        self._password_entry.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize(self):
        self._frame=ttk.Frame(master=self._root)
        self._error_variable=StringVar(self._frame)
        self._error_text=ttk.Label(master=self._frame, textvariable=self._error_variable, foreground='pink')
        self._error_label.grid(padx=10, pady=10)

        self._initialize_username_area()
        self._initialize_password_area()

        login_button = ttk.Button(master=self._frame, text='Login', command=self._login_handler)
        new_user_button=ttk.Button(master=self._frame, text="New user", command=self._handle_new_user_view)

        self._frame.grid_columnconfigure(0,weight=1, minsize=500)
        login_button.grid(padx=10, pady=10, sticky=constants.EW)
        new_user_button.grid(padx=10, pady=10, sticky=constants.EW)

        self._hide_error()


window.title("Login")
ui = LoginView(window)
ui.start()

window.mainloop()