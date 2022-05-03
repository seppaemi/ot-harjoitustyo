"""lisätän tuotteita"""
from tkinter import Tk, ttk, constants, messagebox
from services.service import Service
from entities.item import Item


class AddItemView:
    """Salasanojen lisäyksestä vastaava käyttöliittymäluokka"""

    def __init__(self, root, handle_user_view, user=None):
        """Konstruktori, luo uuden salasanojen lisäyksestä vastaavan näkymän
        """
        self._root = root
        self._frame = None
        self.user = user
        self._handle_user_view = handle_user_view
        self._service = Service()
        self._initialize()

    def pack(self):
        """Pakkaa käyttöliittymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa tämänhetkisen näkymän"""
        self._frame.destroy()

    def handle_back_to_user_view(self):
        """Palauttaa näkymän ShoppinglistViewiin """
        self._handle_user_view(self.user)

    def handle_add_new_item(self, category, amount, item):
        """Lisää uuden salasanan järjestelmään
        """
        if not category or not amount or not item:
            return messagebox.showerror('Error', 'No empty fields allowed')

        user_id = self.user.user_id
        new_item = Item(amount, item, category, user_id)
        result = self._service.add_new_items(new_item)

        messagebox.showinfo('Info', 'Item added')

        self.category_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")
        self.item_entry.delete(0, "end")

        return result

    def _initialize(self):
        """Initialisoi näkymän"""
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Add new credentials", font=(None, 20)
        )
        site_label = ttk.Label(
            master=self._frame, text="category", font=(None, 10)
        )
        self.category_entry = ttk.Entry(
            master=self._frame
        )
        amount_entry = ttk.Label(
            master=self._frame, text="amount or additional info", font=(None, 10)
        )
        self.amount_entry = ttk.Entry(
            master=self._frame
        )
        item_label = ttk.Label(
            master=self._frame, text="item", font=(None, 10)
        )
        self.item_entry = ttk.Entry(
            master=self._frame
        )
        submit_button = ttk.Button(
            master=self._frame,
            text="Submit",
            command=lambda: self.handle_add_new_item(
                self.category_entry.get(),
                self.amount_entry.get(),
                self.item_entry.get()
            )
        )
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=lambda: self.handle_back_to_user_view()
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        site_label.grid(row=1, column=0)
        self.category_entry.grid(
            row=1,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        amount_entry.grid(row=2, column=0)
        self.amount_entry.grid(
            row=2,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        item_label.grid(row=3, column=0)
        self.item_entry.grid(
            row=3,
            column=1,
            sticky=(constants.E, constants.W),
            padx=2,
            pady=2,
            ipady=5
        )

        submit_button.grid(
            row=4,
            column=0,
            sticky=constants.E,
            padx=2,
            pady=5,
            ipady=5
        )
        cancel_button.grid(
            row=4,
            column=1,
            sticky=constants.W,
            padx=2,
            pady=5,
            ipady=5
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
