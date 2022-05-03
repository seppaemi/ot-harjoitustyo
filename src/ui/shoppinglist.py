
"""kauppalistaikkuna
"""
import tkinter as tk
from tkinter import ttk, constants
from services.service import Service


class ShoppinglistView:
    """kauppalistalle"""
    def __init__(self, root, user, handle_login_view, handle_add_item_view):
        """Käyttäjänäkymästä vastaava käyttöliittymäluokka
        """
        self._root = root
        self._frame = None
        self.user = user
        self._service = Service()
        self._handle_login_view = handle_login_view
        self.handle_add_item_view = handle_add_item_view
        self._initialize()

    def pack(self):
        """Pakkaa käyttöliittymän """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa tämänhetkisen näkymän"""
        self._frame.destroy()

    def handle_logout(self):
        """Kirjaa käyttäjän ulos järjestelmästä"""
        message_box = tk.messagebox.askquestion(
            'Info', f'Log out user {self.user.username}?')

        if message_box == 'yes':
            self._handle_login_view()
        else:
            return

    def handle_move_to_add_view(self, user):
        """Siirtää näkymän AddItemViewiin kun nappia painetaan"""
        self.handle_add_item_view(user)

    def insert_to_tree(self):
        """Luo näkymän käyttäjien lisäämille tuotteulle"""
        items = self._service.get_items_by_user(self.user)

        self.number_of_items = 1
        self.iid = 0

        for x in items:
            self.tree.insert(
                '',
                'end',
                iid=self.iid,
                text=self.number_of_items,
                values=(x.category, x.amount, x.item)
            )

            self.iid = self.iid + 1
            self.number_of_items = self.number_of_items + 1

    def _initialize(self):
        """Initialisoi näkymän"""
        self._frame = ttk.Frame(master=self._root)
        style = ttk.Style()

        style.configure('Treeview', rowheight=40)

        add_item_button = ttk.Button(
            master=self._frame,
            text="Add item",
            command=lambda: self.handle_add_item_view(self.user)
        )
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=lambda: self.handle_logout()
        )
        data_label = ttk.Label(
            master=self._frame, text="Saved items", font=(None, 20))

        add_item_button.grid(
            row=0, column=0, sticky=constants.W, padx=5, pady=5)
        logout_button.grid(row=0, column=1, sticky=constants.E, padx=5, pady=5)
        data_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), pady=20)

        self.tree = ttk.Treeview(self._frame, columns=(
            'Site', 'Username', 'Password'))
        self.tree.heading('#0', text='id')
        self.tree.heading('#1', text='Amount')
        self.tree.heading('#2', text='Category')
        self.tree.heading('#3', text="Item")

        self.tree.column('#0', width=30)

        self.tree.grid(row=2, columnspan=4, sticky='nsew')

        self._frame.columnconfigure(0, weight=1, minsize=400)

        self.insert_to_tree()
