
"""kauppalistaikkuna
"""
from tkinter import ttk, constants
from services.service import service

class ItemsView:
    """luokka joka vastaa kauppalistasta"""
    def __init__(self, root, handle_logout):
        """luokan konstruktorit"""
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._create_item_entry = None
        self._frame_for_item_list = None
        self._item_list_view = None

        self._initialize()

    def pack(self):
        """luokan tausta"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """sulkee ikkunan"""
        self._frame.destroy()

    def _logout_handler(self):
        """vastaa sisäänkirjauksesta"""
        service.logout()
        self._handle_logout()

    def _handle_set_item_got(self, item_id):
        """merkkaa tuotteen hankituksi"""
        service.delete_item(item_id)
        self._initialize_item_list()

    def _initialize_item_list(self):
        """auttaa listan kanssa"""
        if self._item_list_view:
            self._item_list_view.destroy()

        items = service.find_items()

        self._item_list_view = ItemListView(
            self._frame_for_item_list,
            items,
            self._handle_set_item_got
        )

        self._item_list_view.pack()

    def _initialize_header(self):
        """nappeja sun muita kivoja
        """
        user_label = ttk.Label(
            master=self._frame,
            text='Shoppinglist'
        )

        logout_button = ttk.Button(
            master=self._frame,
            text='Logout',
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=10, pady=10, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def _handle_create_item(self):
        """nappeja tuotteen luomiseen"""

        item_cont = str(self._create_item_entry.get())

        if item_cont:
            service.add_item(item_cont)
            self._initialize_item_list()
            self._create_item_entry.delete(0, constants.END)

    def _initialize_footer(self):
        """nappeja tuotteen lisäämiseen
        """
        self._create_item_entry = ttk.Entry(master=self._frame)

        _create_item_button = ttk.Button(
            master=self._frame,
            text='Add item',
            command=self._handle_create_item
        )

        self._create_item_entry.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

        _create_item_button.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def _initialize(self):
        """vastaa ulkomuodosta
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame_for_item_list = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_item_list()
        self._initialize_footer()

        self._frame_for_item_list.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)
        self._frame.grid_columnconfigure(1, weight=0)

class ItemListView:
    """luokaa tuotelistalle"""
    def __init__(self, root, items, handle_set_item_got):
        """luokan konstruktorit"""
        self._root = root
        self._items = items
        self._handle_set_item_got = handle_set_item_got
        self._frame = None

        self._initialize()

    def pack(self):
        """taustaa"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """sulkee ikkunan"""
        self._frame.destroy()

    def _initialize_item(self, item):
        """tuotenappeja"""
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame)

        set_done_button = ttk.Button(
            master=item_frame,
            text='got it',
            command=lambda: self._handle_set_item_got(item)
        )

        label.grid(row=0, column=0, padx=10, pady=10, sticky=constants.W)

        set_done_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        """taustajuttuja"""
        self._frame = ttk.Frame(master=self._root)

        for item in self._items:
            self._initialize_item(item)
    