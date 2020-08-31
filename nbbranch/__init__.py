"""nbbranch magic"""
__version__ = '0.0.1'

from .nbbranch import Nbbranch

def load_ipython_extension(ipython):
    ipython.register_magics(Nbbranch)
