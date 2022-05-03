"""hyödynnetään databasea ja buildataan se
"""
from initialize_database import initialize_database


def build():
    """tämä buildaa"""
    initialize_database()


if __name__ == '__main__':
    build()
