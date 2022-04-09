from tkinter import ttk, constants

class AddItemView:
    def __init__(self, root, handle_back=None):
        self._root = root
        self._handle_back = handle_back
        self._frame = None

        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header=ttk.Label(master=self._frame, text="Create user")
        header.grid(columnspan=2, sticky=constants.W, padx=10, pady=10)

        item=ttk.Label(master=self._frame, text="Name of the item")
        item_write=ttk.Entry(master=self._frame)

        item.grid(padx=10, pady=10)
        item_write.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=10, pady=10)

        button=ttk.Button(master=self._frame, text="Back", command=self._handle_back)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=10, pady=10)
        
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
