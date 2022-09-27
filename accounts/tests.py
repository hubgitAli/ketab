from django.test import TestCase

from django.urls import reverse
from django.contrib.auth import get_user_model

class TestAccountsApp(TestCase):
    username = 'new_user'  # i can defin a variable in my class to use in evry where in class's functions
    email = '@anything.com'

    def test_signup_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_contain_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response,'registration/signup.html')

########################################################

    def test_login_by_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_contain_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')


    def test_signin_form(self):
        user = get_user_model().objects.create_user(
            self.username,  # i write that instead of this 'new_user',
            self.email, # i write that instead of this '@anything.com',
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

