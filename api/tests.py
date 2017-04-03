import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class UserResourceTest(TestCase):
    """
    Tests the CRUD methods in user resource.
    """
    def create_user(self):
        """
        helper method for creating users
        """
        user_create_url = reverse('user-list')
        # first create a user
        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        return user

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

    def test_user_can_retrieve_user_list(self):
        """
        test that a user can view a list of users using get(list)
        """
        user_create_url = reverse('user-list')
        # first create a user
        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        # then perform the get(list)
        response = self.client.get(user_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('testuser' in response.content.decode('ascii'))

    def test_user_can_retrieve_a_single_user(self):
        """
        test that a user can view a single user
        """
        user_create_url = reverse('user-list')
        # first create a user
        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        # then perform the get(detail), but first, we need the user's id
        user_obj = User.objects.filter(username=user['username'])[0]
        user_get_detail = reverse('user-detail', kwargs={'pk': user_obj.id})
        response = self.client.get(user_get_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('testuser' in response.content.decode('ascii'))

    def test_user_can_edit_user_detail(self):
        """
        test that a user can edit user details
        """
        user = self.create_user()
        user_obj = User.objects.filter(username=user['username'])[0]
        user_put_detail = reverse('user-detail', kwargs={'pk': user_obj.id})
        new_data = {
            'username': "testuser",
            'password': "67890"
        }
        json_data = json.dumps(new_data)
        response = self.client.put(
            user_put_detail, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_user_detail(self):
        """
        test that a user can delete user from database
        """
        user = self.create_user()
        user_obj = User.objects.filter(username=user['username'])[0]
        user_delete_url = reverse('user-detail', kwargs={'pk': user_obj.id})
        response = self.client.delete(user_delete_url)
        self.assertEqual(response.status_code, 204)

    def test_user_can_access_token(self):
        """
        test that a user can input username and password and access token
        """
        user = self.create_user()
        login_url = reverse('api-auth')

        response = self.client.post(login_url, user)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.content.decode('ascii'))