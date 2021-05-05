from tests.v1.base_test import BaseTest


class TestHomeViews(BaseTest):
    """Test views."""

    def test_index(self):
        """Test the index view endpoint."""

        response = self.client.get('/api/v1/home', follow_redirects=True)
        assert response.status_code == 200
