from django.test import TestCase

from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_home_page_content_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'home')

    def test_home_page_content_by_url(self):
        response = self.client.get('')
        self.assertContains(response, 'home')

    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_template_url(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

