"""Urls of properties."""

# Views
from .views import PropertiesView

properties = PropertiesView()


def url_resolver(path: str, request_type: str, query_params: dict = None):
    """Return the url of the view.

    Args:
        path (str): The path of the view.
        request_type (str): The request type.
        query_params (dict, optional): The query parameters. Defaults to None.

    Returns:
        the status code and the data of the request.
    """
    if request_type == 'GET':
        paths = [
            ('/properties', properties.get(query_params)),
        ]
        if any(path in url for url in paths):
            return paths[0][1].status_code, paths[0][1].data
        else:
            return 404, 'URL not found'
    else:
        return 405, 'Method not allowed'
