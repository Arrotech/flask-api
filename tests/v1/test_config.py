import os
import unittest
from flask import current_app
from flask_testing import TestCase
from run import app
from instance.config import app_config


class TestDevelopmentConfig(TestCase):

    """Test development configurations."""

    def create_app(self):
        app.config.from_object(app_config['development'])
        return app

    def test_development_configurations(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']
                        == os.environ.get('DATABASE_URI'))


class TestProductionConfig(TestCase):

    """Test production configurations."""

    def create_app(self):
        app.config.from_object(app_config['production'])
        return app

    def test_production_configurations(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']
                        == os.environ.get('DATABASE_URI'))


class TestTestingConfig(TestCase):

    """Test testing configurations."""

    def create_app(self):
        app.config.from_object(app_config['testing'])
        return app

    def test_testing_configurations(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']
                        == os.environ.get('TEST_DATABASE_URI'))


class TestStagingConfig(TestCase):

    """Test staging configurations."""

    def create_app(self):
        app.config.from_object(app_config['staging'])
        return app

    def test_staging_configurations(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']
                        == os.environ.get('DATABASE_URI'))


class TestReleaseConfig(TestCase):

    """Test release configurations."""

    def create_app(self):
        app.config.from_object(app_config['release'])
        return app

    def test_release_configurations(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI']
                        == os.environ.get('DATABASE_URI'))


if __name__ == '__main__':
    unittest.main()
