from .system import System777
from . import database
from . import numbers

# Initialize the system
system = System777(
    goddesses=database.goddesses, angels=database.angels, demons=database.demons
)
