from django.test import TestCase
from django.urls import reverse
from .models import Post, Post1

class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text="mano")

    def test_t(self):
        post = Post.objects.get(id=1)
        title_test = f"{ post.title }"
        text_test = f'{ post.text }'
        self.assertEqual(title_test, 'Mavzu')
        self.assertEqual(text_test, 'mano')

class Post1Test(TestCase):
    def setUp(self):
        Post1.objects.create(title='Mavzu', text="mano")

    def test_t(self):
        post = Post1.objects.get(id=2)
        title_test = f"{ post1.title }"
        text_test = f'{ post1.text }'
        self.assertEqual(title_test, 'Mavzu')
        self.assertEqual(text_test, 'mano')