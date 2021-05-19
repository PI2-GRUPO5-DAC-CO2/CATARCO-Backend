from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TesteUsuario(TestCase):
    def testa_usuario(self):
        user = User.objects.create_user("user1", "user1@test.com", "password123")
        user.save()

        user = User.objects.get(username="user1")

        self.assertEqual(f'{user.username} {user.email}', 'user1 user1@test.com')
