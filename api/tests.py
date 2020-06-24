import json

from django.urls import reverse

from rest_framework.test import APITestCase

from api import models


# Create your tests here.
class UserResourceTest(APITestCase):
    """
    Tests the CRUD methods in user resource.
    """
    def create_user(self):
        """
        helper method for creating users
        """
        user_create_url = reverse('notesuser-list')
        # first create a user
        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        return user

    def login_user(self, user):
        """
        helper method for user login
        """
        login_url = reverse('api-auth')
        response = self.client.post(login_url, user)
        json_data = json.loads(response.content.decode('ascii'))
        return json_data['token']

    def test_user_can_create_profile(self):
        """
        Test that user can perform a POST operation on this resource.
        """
        user_create_url = reverse('notesuser-list')

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
        user_create_url = reverse('notesuser-list')
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
        user_create_url = reverse('notesuser-list')
        # first create a user
        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        # then perform the get(detail), but first, we need the user's id
        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]
        user_get_detail = reverse('notesuser-detail', kwargs={'pk': user_obj.id})
        response = self.client.get(user_get_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('testuser' in response.content.decode('ascii'))

    def test_user_can_edit_user_detail(self):
        """
        test that a user can edit user details
        """
        user = self.create_user()
        token = self.login_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        
        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]
        user_put_detail = reverse('notesuser-detail', kwargs={'pk': user_obj.id})
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
        token = self.login_user(user)

        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]
        user_delete_url = reverse('notesuser-detail', kwargs={'pk': user_obj.id})
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = self.client.delete(user_delete_url)
        self.assertEqual(response.status_code, 204)


class NotesResourceTest(APITestCase):
    """
    Tests the CRUD methods in notes resource.
    """
    def create_user(self):
        """
        helper method for creating users
        """
        user_create_url = reverse('notesuser-list')
        # first create a user
        user = {
            "username": "testuser",
            "password": "12345"
        }
        response = self.client.post(user_create_url, user)
        return user

    def login_user(self, user):
        """
        helper method for user login
        """
        login_url = reverse('api-auth')
        response = self.client.post(login_url, user)
        json_data = json.loads(response.content.decode('ascii'))
        return json_data['token']

    def create_note(self, token):
        """
        helper method for creating notes
        """
        note_create_url = reverse('notes-list')
        note = {
            'title': 'Test create note',
            'note': 'This note was created in the helper function',
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = self.client.post(note_create_url, note)
        return note

    def test_user_can_create_note(self):
        """
        test that a user can create a note
        """
        user = self.create_user()
        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]

        note_create_url = reverse('notes-list')
        note = {
            'title': 'Test note',
            'note': 'The quick brown fox',
            'owner': user_obj.id
        }
        token = self.login_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        response = self.client.post(note_create_url, note)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(note['title'] in response.content.decode('ascii'))
        self.assertTrue(note['note'] in response.content.decode('ascii'))

    def test_user_can_view_notes_list(self):
        """
        test user can view a list of notes
        """
        user = self.create_user()
        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]
        token = self.login_user(user)

        note = self.create_note(token)
        
        note_get_list_url = reverse('notes-list')
        response = self.client.get(note_get_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(note['title'] in response.content.decode('ascii'))
        self.assertTrue(
            "{0}".format(user_obj.id) in response.content.decode('ascii'))
        self.assertTrue(note['note'] in response.content.decode('ascii'))

    def test_user_can_view_a_notes_object_details(self):
        """
        test user can view the details of a note
        """
        user = self.create_user()
        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]
        token = self.login_user(user)

        note = self.create_note(token)
        note_obj = models.Notes.objects.filter(title=note['title'])[0]
        
        note_get_list_url = reverse(
            'notes-detail', kwargs={'pk': note_obj.id})
        response = self.client.get(note_get_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(note['title'] in response.content.decode('ascii'))
        self.assertTrue(
            "{0}".format(note_obj.owner.id) in response.content.decode('ascii'))
        self.assertTrue(note['note'] in response.content.decode('ascii'))

    def test_user_can_edit_note_detail(self):
        """
        test that a user can edit note details
        """
        user = self.create_user()
        user_obj = models.User.objects.filter(username=user['username'])[0]
        token = self.login_user(user)

        note = self.create_note(token)
        note_obj = models.Notes.objects.filter(title=note['title'])[0]

        new_note_data = {
            'title': 'Editing a new note object',
            'note': 'We are testing the ability to edit details in a note',
            'owner': user_obj.id
        }

        note_put_detail = reverse('notes-detail', kwargs={'pk': note_obj.id})
        
        json_data = json.dumps(new_note_data)
        response = self.client.put(
            note_put_detail, json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            new_note_data['title'] in response.content.decode('ascii'))
        self.assertTrue(
            "{0}".format(new_note_data['owner']) in response.content.decode(
                'ascii')
        )
        self.assertTrue(
            new_note_data['note'] in response.content.decode('ascii'))
        self.assertFalse(note['title'] in response.content.decode('ascii'))
        self.assertFalse(note['note'] in response.content.decode('ascii'))

    def test_user_can_delete_note(self):
        """
        tests that a user can delete a note
        """
        user = self.create_user()
        user_obj = models.NotesUser.objects.filter(username=user['username'])[0]
        token = self.login_user(user)

        note = self.create_note(token)
        note_obj = models.Notes.objects.filter(title=note['title'])[0]

        note_delete_url = reverse('notes-detail', kwargs={'pk': note_obj.id})
        response = self.client.delete(note_delete_url)
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
