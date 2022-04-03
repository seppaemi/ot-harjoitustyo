from tkinter import ttk, constants
from tkinter import Tk
window=Tk()
window.title("Login")

class LoginView:
    def __init__(self, root, handle_login=None, handle_show_new_user_view=None):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_new_user_view = handle_show_new_user_view
        self._frame = None
        self._username_box = None
        self._password_box = None
        self._error_variable = None
        self._error_text = None

        self._initialize()

    def start(self):
        self._frame.pack(fill=constants.X)
    
    def bgcolor(self):
        bgcolor(color='pink')

    def remove(self):
        self._frame.remove()

    def _login_handler(self):
        username = self._username_box.get()
        password = self._password_box.get()

    def _initialize_username_area(self):
        username_text = ttk.Label(master=self._frame, text='Username', foreground= 'black', background='pink')
        self._username_box = ttk.Entry(master=self._frame)

        username_text.grid(padx=10, pady=10, sticky=constants.W)
        self._username_box.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize_password_area(self):
        password_text = ttk.Label(master=self._frame, text='Password', foreground='black', background='pink')
        self._password_box = ttk.Entry(master=self._frame)

        password_text.grid(padx=10, pady=10, sticky=constants.W)
        self._password_box.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_username_area()
        self._initialize_password_area()

        login_button = ttk.Button(master=self._frame,text='Login',command=self._login_handler)
        create_user_button = ttk.Button(master=self._frame,text="Create user",command=self._handle_show_new_user_view,)

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

ui = LoginView(window)
window.configure(bg='pink')
ui.start()

window.mainloop()