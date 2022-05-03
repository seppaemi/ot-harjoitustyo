"""tämä avaa sovellus sivun
"""
from tkinter import Tk
from ui.ui import UI


def main():
    """kaikki tarvittava sivun avaukseen
    """
    window = Tk()
    window.title('Shoppinglist')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
