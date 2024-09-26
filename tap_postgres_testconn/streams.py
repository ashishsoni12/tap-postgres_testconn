from typing import Any, Dict, Optional, Iterable
from singer_sdk.streams import Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
from tap_postgres_testconn.client import create_postgres_engine
from .globals import addition
import json
from datetime import datetime
from tap_postgres_testconn.conversion import convert_epoch_to_format
import logging
LOGGER = logging.getLogger(__name__)
import time
import os
class PostgrestestconnStream(Stream):
    """Base stream class for tap-postgres using SQLAlchemy."""

    # Define the name of the stream
    name = "postgrestestconn_stream"
    schema = th.PropertiesList(
        th.Property("data", th.ObjectType())
    ).to_dict()

    
    
    def __init__(self, tap, table_name: Optional[str] = None):
        super().__init__(tap)
        self.engine = create_postgres_engine(self.config)
        

    def get_records(self, context: Optional[Dict] = None) -> Iterable[Dict[str, Any]]:

      # Construct the SQL query
      query="SELECT 1;"
      with self.engine.connect() as conn:

        self.logger.info(f"Executing query: {query}")
        result = conn.execute(text(query))
        column_names = list(result.keys()) # Retrieve column names
        x={}
        row = result.fetchone()  # We expect a single row with the value `1`

        if row:
                self.logger.info(f"Connection successful! Query result: {row[0]}")
                # Yield a simple response to indicate success
                yield {"connection_status": "success", "query_result": row[0]}
        else:
                self.logger.info("No result returned.")
                yield {"connection_status": "failure", "query_result": None}

    def post_process(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Adjust records after they are retrieved, if necessary."""
        return record


    def get_new_pkey(self, record: Dict) -> Any:
        return record.get("id")

