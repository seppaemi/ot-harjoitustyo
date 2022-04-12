"""tässä tapahtuu kaikkien muiden sivun luomisten yhdistys
"""
from ui.login import LoginView
from ui.shoppinglist import ShoppinglistView
from ui.new_user import CreateUserView


class UI:
    """luokka UI:lle
    """
    def __init__(self, root):
        """alustaa tarvittavat
        """
        self.root = root
        self.current_view = None

    def start(self):
        """näyttää tyjän aloitus-näytön
        """
        self._show_login_view()

    def _hide_current_view(self):
        """sulkee tarvittavan sivun
        """
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def _show_login_view(self):
        """näyttää kirjautumissivun
        """
        self._hide_current_view()
        self.current_view = LoginView(self.root,
            self._show_items_view, self._show_create_user_view)
        self.current_view.pack()

    def _show_items_view(self):
        """näyttää"""
        self._hide_current_view()
        self.current_view = ShoppinglistView(self.root, self._show_login_view)
        self.current_view.pack()

    def _show_create_user_view(self):
        """näyttää luo käyttäjä-sivun
        """
        self._hide_current_view()
        self.current_view = CreateUserView(self.root, self._show_items_view,self._show_login_view)
        self.current_view.pack()
