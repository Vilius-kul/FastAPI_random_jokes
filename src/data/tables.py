from venv import create

from piccolo.columns.column_types import Text, Timestamp
from piccolo.table import Table


class JokesEnglish(Table, tablename="jokes_in_english"):
    joke = Text()
    created_at = Timestamp()
