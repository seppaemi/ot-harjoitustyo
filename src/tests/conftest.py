"""conftest dokumentti testejä varten
"""
from build import build


def pytest_configure():
    """build testeihin
    """
    build()
