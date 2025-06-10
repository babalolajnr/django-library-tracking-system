from django.test import TestCase
from rest_framework.test import APITestCase


class LibraryAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="john", password="secret")
