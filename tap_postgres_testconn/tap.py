from typing import List
from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_postgres_testconn.streams import PostgrestestconnStream
STREAM_TYPES = [
    PostgrestestconnStream

]

class Tappostgres_testconn(Tap):
    """PostgreSQL tap class."""
    name = "tap-postgres_testconn"

    config_jsonschema = th.PropertiesList(
        th.Property("host", th.StringType, required=True, description="PostgreSQL host"),
        th.Property("port", th.IntegerType, required=True, description="PostgreSQL port"),
        th.Property("database", th.StringType, required=True, description="PostgreSQL database name"),
        th.Property("user", th.StringType, required=True, description="PostgreSQL user"),
        th.Property("password", th.StringType, required=True, description="PostgreSQL password"),

    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        # Pass `self` to ensure it's the right type
        return [PostgrestestconnStream(tap=self)]

