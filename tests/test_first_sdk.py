import unittest

from first_sdk.first_sdk import FirstSdk


class TestFirstSdk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #  FirstSdk.set_default_proxy("http://localhost:8080")
        cls.api = FirstSdk()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_crud_items(self):
        """
        Test the creation, reading, update and deletion of an item.
        """
        response = self.api.create_item("ItemName", "Some description")
        self.assertEqual(response.status, 201)
        item_id = response.data["pk"]
        self.assertEqual("ItemName", response.data["name"])
        self.assertEqual("Some description", response.data["description"])

        response = self.api.get_items()
        self.assertEqual(response.status, 200)
        self.assertIn("results", response.data)
        self.assertTrue(isinstance(response.data["results"], list))

        response = self.api.get_items(item_id)
        self.assertEqual(response.status, 200)
        self.assertEqual("ItemName", response.data["name"])
        self.assertEqual("Some description", response.data["description"])

        response = self.api.update_item(item_id, "New name")
        self.assertEqual(response.status, 200)
        self.assertEqual("New name", response.data["name"])
        self.assertEqual("Some description", response.data["description"])

        response = self.api.delete_item(item_id)
        self.assertEqual(response.status, 204)
