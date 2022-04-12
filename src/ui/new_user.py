"""luodaan ikkuna käyttäjän luomiselle
"""
from tkinter import ttk, StringVar, constants
from services.service import service, UsernameExistsError

class CreateUserView:
    """luokka ikkunna luomiselle
    """
    def __init__(self, root, handle_create_user, handle_show_login_view):
        """alustaa kaiken tarvittavan
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_text = None
        self._password_text = None
        self._error_variable = None
        self._error_label = None
        self._initialize()

    def pack(self):
        """luo ikkunan
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """sulkee ikkunan
        """
        self._frame.destroy()

    def _create_user_handler(self):
        """kirjoitusmahdollisuus tunnukselle ja salasanalle
        """
        username = self._username_text.get()
        password = self._password_text.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error('Username and password is required')
            return
        try:
            service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f'Username {username} already exists')

    def _show_error(self, message):
        """näyttää virheilmoituksen tarvittaessa
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """poistaa virheilmoituksen tarvittaessa
        """
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """luo tunnukselle kentän
        """
        username_label = ttk.Label(master=self._frame, text='Username')
        self._username_text = ttk.Entry(master=self._frame)

        username_label.grid(padx=10, pady=10, sticky=constants.W)
        self._username_text.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize_password_field(self):
        """luo salasanalle kentän
        """
        password_label = ttk.Label(master=self._frame, text='Password')
        self._password_text = ttk.Entry(master=self._frame)

        password_label.grid(padx=10, pady=10, sticky=constants.W)
        self._password_text.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize(self):
        """luodaan koko sivu"""
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame,
            textvariable=self._error_variable, foreground='red')

        self._error_label.grid(padx=10, pady=10)

        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(master=self._frame,
            text='Create', command=self._create_user_handler)
        login_button = ttk.Button(master=self._frame,
            text='Login', command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        create_user_button.grid(padx=10, pady=10, sticky=constants.EW)
        login_button.grid(padx=10, pady=10, sticky=constants.EW)

        self._hide_error()
