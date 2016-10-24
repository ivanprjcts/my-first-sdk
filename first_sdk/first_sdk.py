from sdklib.http import HttpSdk
from sdklib.util.parser import safe_add_end_slash, parse_args


class FirstSdk(HttpSdk):
    """
    My First Sdk.
    """
    DEFAULT_HOST = "http://127.0.0.1:8000"

    API_ITEMS_URL_PATH = "/items/"

    def create_item(self, name, description=None):
        """
        Create an item.
        :param name: str
        :param description: str (optional)
        :return: SdkResponse
        """
        params = parse_args(name=name, description=description)
        return self._http_request("POST", self.API_ITEMS_URL_PATH, body_params=params)

    def get_items(self, item_id=None):
        """
        Retrieve all items if 'item_id' is None. Otherwise, get specified item by 'item_id'.
        :param item_id: int (optional)
        :return: SdkResponse
        """
        return self._http_request("GET", self.API_ITEMS_URL_PATH + safe_add_end_slash(item_id))

    def update_item(self, item_id, name, description=None):
        """
        Update an item.
        :param item_id: int
        :param name: str
        :param description: str (optional)
        :return: SdkResponse
        """
        params = parse_args(name=name, description=description)
        return self._http_request("PUT", "%s%d/" % (self.API_ITEMS_URL_PATH, item_id), body_params=params)

    def delete_item(self, item_id):
        """
        Remove an item.
        :param item_id: int
        :return: SdkResponse
        """
        return self._http_request("DELETE", "%s%d/" % (self.API_ITEMS_URL_PATH, item_id))
