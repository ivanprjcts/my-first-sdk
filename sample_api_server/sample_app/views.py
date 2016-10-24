from rest_framework.views import APIView
from rest_framework.response import Response


class ItemsView(APIView):
    """
    View to list all items in the system.
    """
    def get(self, request, format=None):
        """
        Return a list of all items.
        """
        items = [
            {
                "pk": 1,
                "name": "item",
                "description": ""
            },
            {
                "pk": 2,
                "name": "ItemName",
                "description": "Some description"
            }
        ]
        return Response(items)

    def post(self, request, format=None):
        """
        Return a default model.
        """
        item_name = request.data.get("name", None)
        item_description = request.data.get("description", None)
        item = {"pk": 1, "name": item_name, "description": item_description}
        return Response(item, status=201)


class ItemDetailView(APIView):
    def get(self, request, pk=None, format=None):
        """
        Return a list of all items.
        """
        items = {
                "pk": 2,
                "name": "ItemName",
                "description": "Some description"
            }
        return Response(items)

    def put(self, request, pk=None, format=None):
        """
        Return a list of all items.
        """
        item_name = request.data.get("name", None)
        item_description = request.data.get("description", None)
        item = {"pk": 1, "name": item_name, "description": item_description}
        return Response(item)

    def delete(self, request, pk=None, format=None):
        """
        Return a list of all items.
        """
        return Response(status=204)
