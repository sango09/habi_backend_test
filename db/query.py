"""Queries for the database."""

# DB connection
from db.db_connection import db_connection as db


class RawQuery:
    def __init__(self):
        self.db = db

    def _execute_query(self, query_string: str) -> list:
        """
        Execute the query and return the result.
        """
        cursor = self.db.cursor(buffered=True, dictionary=True)
        cursor.execute(query_string)
        cursor.close()
        return cursor.fetchall()

    def fetch_all_properties(self, query_params: dict = None):
        """
        Fetch all properties from the database.
        """
        base_query = '''
        SELECT address, city, name as status, price, description
        FROM ((status_history
            INNER JOIN status ON status_history.status_id = status.id)
                 INNER JOIN property ON status_history.property_id = property.id)
        WHERE update_date IN (
            SELECT max(update_date) AS date
            FROM status_history
            GROUP BY property_id)
          AND status.name IN ('pre_venta', 'en_venta', 'vendido')
        '''
        if query_params is not None:
            for key, value in query_params.items():
                if key == 'status':
                    base_query += f" AND status.name = '{value[0]}'"
                elif key == 'year':
                    base_query += f" AND property.year = {int(value[0])}"
                elif key == 'city':
                    base_query += f" AND property.city = '{value[0]}'"

        return self._execute_query(base_query)
