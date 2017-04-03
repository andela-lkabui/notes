from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class UserResourceTest(TestCase):
    """
    Tests the CRUD methods in user resource.
    """

    def test_user_can_create_profile(self):
        """
        Test that user can perform a POST operation on this resource.
        """
        user_create_url = reverse('user-list')

        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        self.assertEqual(response.status_code, 201)
        self.assertTrue('username' in response.content.decode('ascii'))
        self.assertTrue(user['username'] in response.content.decode('ascii'))
        
