import json
import unittest

from category_mapper import app, drop_database
from category_mapper.models import models


class TestResources(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        with self.app_context:
            models.db.create_all()
        self.app_client = app.test_client()

    def tearDown(self):
        with self.app_client.application.app_context():
            drop_database()

    def test_get_category_request_1(self):
        input_category = 'Mens+clothing'
        expected = {"normalised_category": "/Men/Clothing"}

        response = self.app_client.get("/category/{}".format(input_category))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()), expected)

    def test_get_category_request_2(self):
        input_category = 'adult+-+female+-+jewelry+and+watches+-+fashion+jewelry'
        expected = {"normalised_category": "/Women/Jewellery"}

        response = self.app_client.get("/category/{}".format(input_category))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()), expected)

    def test_post_category_request_201(self):
        input_category = 'Mens+clothing'
        expected = {
            "retailer_category": input_category,
            "normalised_category": "/Men/Clothing"
        }

        response = self.app_client.post("/category/{}".format(input_category))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data.decode()), expected)

    def test_post_category_request_200(self):
        input_category = 'adult+-+female+-+jewelry+and+watches+-+fashion+jewelry'
        expected = {
            "retailer_category": input_category,
            "normalised_category": "/Women/Jewellery"
        }

        response = self.app_client.post("/category/{}".format(input_category))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data.decode()), expected)

        response = self.app_client.post("/category/{}".format(input_category))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode()), expected)
