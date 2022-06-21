from urllib import response
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 2)
    
    def test_read_one_product(self):
        response = self.client.get(f"/api/v1/products/1")
        self.assertEqual(response.status_code, 200)
    
    def test_no_matching_products(self):
        response = self.client.get(f"/api/v1/products/:id")
        self.assertEqual(response.status_code, 404)
        self.assertIsNone(response.json)