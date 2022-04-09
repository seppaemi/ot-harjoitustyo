from tkinter import ttk, constants, Tk

class ShoppinglistView:
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
        header=ttk.Label(master=self._frame, text="Items needed")
        header.grid(columnspan=2, sticky=constants.W, padx=10, pady=10)

        button1=ttk.Button(master=self._frame, text="Log out", command=self._handle_login)
        button2=ttk.Button(master=self._frame, text="Add item")
        button1.grid(columnspan=2, sticky=(constants.E, constants.W), padx=10, pady=10)
        button2.grid(columnspan=2, sticky=(constants.E, constants.W), padx=10, pady=10)
        
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
