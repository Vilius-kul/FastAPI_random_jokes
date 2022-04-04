from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={"user": "Vilius", "password": "12345", "database": "jokes_pg"}
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["jokes_piccoloapp.piccolo_app"])
