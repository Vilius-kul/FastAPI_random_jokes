from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Text, Timestamp
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod

ID = "2022-04-05T10:33:36:146365"
VERSION = "0.70.1"
DESCRIPTION = "Add JokesEnglish table"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="jokes", description=DESCRIPTION
    )

    manager.add_table("JokesEnglish", tablename="jokes_in_english")

    manager.add_column(
        table_class_name="JokesEnglish",
        tablename="jokes_in_english",
        column_name="joke",
        db_column_name="joke",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="JokesEnglish",
        tablename="jokes_in_english",
        column_name="created_at",
        db_column_name="created_at",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampNow(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
