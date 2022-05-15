"""kauppalistaikkuna
"""
import tkinter as tk
from tkinter import ttk, constants
from services.service import Service


class ShoppinglistView:
    """kauppalistalle
    """
    def __init__(self, root, user, handle_login_view, handle_add_item_view):
        """Käyttäjänäkymästä vastaava käyttöliittymäluokka
        Args:
            root: Juurielementti, joka hallitsee nykyistä näkymää
            user: User-luokan olio
            handle_login_view: UI-luokan metodi, joka siirtää näkymän LoginViewiin
            handle_add_password_view: UI-luokan metodi, joka siirtää näkymän AddPasswordViewiin
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

        for item in items:
            self.tree.insert(
                '',
                'end',
                iid=self.iid,
                text=self.number_of_items,
                values=(item.category, item.amount, item.item)
            )

            self.iid = self.iid + 1
            self.number_of_items = self.number_of_items + 1

    def remove_selected(self, item):
        """poistaa tuotteita"""
        self._service.delete_item(item)
        self.tree.delete(item)

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

        remove_selected_button=ttk.Button(master=self._frame ,
            text="remove selected item", command=lambda:
            self.remove_selected(self.tree.selection()[0])
            )

        remove_selected_button.grid(
            row=0, column=2, sticky=constants.W, padx=5, pady=5)

        self.tree = ttk.Treeview(self._frame, columns=(
            'amount', 'category', 'item'))
        self.tree.heading('#0', text='id')
        self.tree.heading('#1', text='Amount')
        self.tree.heading('#2', text='Item')
        self.tree.heading('#3', text="Category")

        self.tree.column('#0', width=30)

        self.tree.grid(row=2, columnspan=4, sticky='nsew')

        self._frame.columnconfigure(0, weight=1, minsize=400)

        self.insert_to_tree()
        