"""uuden jäsenne luomiselle"""
from tkinter import ttk, constants, messagebox
from services.service import Service
from entities.user import User


class RegisterView:
    """rekisteröinti ikkuna"""
    def __init__(self, root, handle_login_view):
        """Rekisteröitymisnäkymästä vastaava käyttöliittymäluokka
        Args:
            root: Juurielementti, joka hallitsee nykyistä näkymää
            handle_login_view: UI-luokan metodi, joka siirtää näkymän LoginViewiin
        """
        self._root = root
        self._frame = None
        self._initialize()
        self._handle_login_view = handle_login_view
        self._service = Service()

    def pack(self):
        """Pakkaa käyttöliittymän komponentit"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa tämänhetkisen näkymän"""
        self._frame.destroy()

    def _handle_register(self, username, password):
        """Huolehtii uuden käyttäjän rekisteröinnistä, heittää virheen virheellisellä syötteellä
        """
        if len(username) > 10:
            return messagebox.showerror('Error', 'Username must be under 10 characters long')

        if len(password) > 20:
            return messagebox.showerror('Error', 'Password must be under 20 characters long')

        user = self._service.create_user(User(username, password))

        if not username or not password:
            return messagebox.showerror('Error', 'Fill all fields')

        if not user:
            return messagebox.showerror('Error', 'User already exists')

        self._handle_login_view()
        return user

    def _handle_cancel(self):
        """Siirtää näkymän LoginViewiin kun nappia painetaan"""
        self._handle_login_view()

    def _initialize(self):
        """Initialisoi näkymän"""
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Register", font=(None, 20)
        )
        username_label = ttk.Label(
            master=self._frame, text="username", font=(None, 10)
        )
        username_entry = ttk.Entry(
            master=self._frame
        )
        password_label = ttk.Label(
            master=self._frame, text="password", font=(None, 10)
        )
        password_entry = ttk.Entry(
            master=self._frame, show="*"
        )
        # add user to database and return to login screen
        register_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=lambda: self._handle_register(
                username_entry.get(), password_entry.get()
            )
        )
        # return to login screen
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=lambda: self._handle_cancel()
        )

        heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        username_label.grid(
            row=1, column=0
        )
        username_entry.grid(
            row=1,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )
        password_label.grid(
            row=2, column=0
        )
        password_entry.grid(
            row=2,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )
        register_button.grid(
            row=3,
            column=0,
            sticky=constants.E,
            padx=2,
            pady=5,
            ipady=5
        )
        cancel_button.grid(
            row=3,
            column=1,
            sticky=constants.W,
            padx=2,
            pady=5,
            ipady=5
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
