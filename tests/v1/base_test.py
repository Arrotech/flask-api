import unittest
from app import create_app
# from app.extensions import db


class BaseTest(unittest.TestCase):
    """Set up and tear down app for testing."""

    def setUp(self):
        """Set up the app for testing."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # db.create_all()

    def tearDown(self):
        """Tear down the app after testing."""
        self.app_context = self.app.app_context()
        self.app_context.push()
        # db.drop_all()
