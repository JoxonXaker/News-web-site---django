from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='Yangiliklar matni')

    def test_tetx_context(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, 'Yangiliklar matni')


class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text='Boshqa Yangiliklar matni')

    def test_view_url_exist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')