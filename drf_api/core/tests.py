from django.test import TestCase
from .models import Core
from django.contrib.auth import get_user_model


# Create your tests here.
class CoreTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        test_core = Core.objects.create(name="rake", wner=testuser1, description="Better than shovel for leaves.")
        test_core.save()

    def test_things_model(self):
        thing = Core.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(actual_description, "Better than shovel for leaves.")