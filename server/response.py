"""Basic response data"""

# Python
import json


class Response:
    """Basic response data

    Args:
        data (list): The data that need to json.
        status (int): status code of the response.

    return the data in JSON format and the status code
    """

    def __init__(self, data: list, status: int):
        self.status_code = status
        self.data = data

    def to_json(self):
        data = json.dumps(self.data)
        return data, self.status_code
