"""View of properties."""

# Queries
from db import RawQuery

# server
from server import Response


class PropertiesView:
    """View of properties."""

    def get(self, query_params: dict = None):
        """Get all properties from the database."""
        data = RawQuery().fetch_all_properties(query_params)
        return Response(data, status=200)
