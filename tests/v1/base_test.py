import unittest
from app import create_app
from app.extensions import db


class BaseTest(unittest.TestCase):
    """Set up and tear down app for testing."""

    def setUp(self):
        """Set up the app for testing."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Tear down the app after testing."""
        with self.app.app_context():
            db.drop_all()
