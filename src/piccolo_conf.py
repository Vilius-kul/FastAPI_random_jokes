from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "jokes_pg",
        "user": "admin",
        "password": "admin123",
        "host": "postgres-db",
        "port": "5432",
    }
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=["data.piccolo_app"])
