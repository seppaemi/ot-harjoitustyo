from tkinter import ttk, constants

class CreateUserView:
    def __init__(self, root, handle_login=None):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header=ttk.Label(master=self._frame, text="Create user")
        header.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username=ttk.Label(master=self._frame, text="Username")
        username_text=ttk.Entry(master=self._frame)

        username.grid(padx=5, pady=5)
        username_text.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password=ttk.Label(master=self._frame, text="Password")
        password_text=ttk.Entry(master=self._frame, show="*")

        password.grid(padx=5, pady=5)
        password_text.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button=ttk.Button(master=self._frame, text="Create user", command=self._handle_login)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
