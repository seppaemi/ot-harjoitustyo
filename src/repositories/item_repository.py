from entities.item import Item
from entities.user import User
def get_id_by_row(row):
    return row['id'] if row else None

def get_name_by_row(row):
    return row['name'] if row else None

class ShoppinglistRepository:
    def __init__(self):
        pass