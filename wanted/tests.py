import jwt

from django.test                    import TestCase, Client
from unittest.mock                  import MagicMock, patch

from .models           import User, Post
from my_settings       import SECRET_KEY

class PostTest(TestCase):
    def setUp(self):
        User.objects.create(
            id       = 1,
            email    = 'wecode@wanted.com',
            password = 'wecode12#',
        )
        post = Post.objects.create(
            id       = 1,
            text     = '예쓰예쓰요',
        )
        post.created_at = '2021-08-19T11:03:10.216Z'
        post.save()
    
    def tearDown(self):
        Post.objects.all().delete(),
        User.objects.all().delete(),