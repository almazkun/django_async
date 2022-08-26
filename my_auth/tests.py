from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from my_auth.serializers import UserSerializer
from my_auth.views import UserViewSet


# Create your tests here.
class TestSerializer(TestCase):
    def test_user_serializer(self):
        user_data = {"email": "asd@email.com", "username": "some"}

        UserSerializer().create(user_data)

        user = get_user_model().objects.get(**user_data)

        self.assertEqual(
            user.email,
            user_data.get("email"),
        )
        self.assertEqual(user.username, user_data.get("username"))


class TestViews(TestCase):
    def test_user_view_set(self):
        req = APIRequestFactory().get(reverse("user-list"))
        get_user_model().objects.bulk_create(
            [
                get_user_model()(email="asd@email.com", username="qwe"),
                get_user_model()(email="zxc@email.com", username="asd"),
            ]
        )
        res = UserViewSet.as_view({"get": "list"})(req)

        user_list = get_user_model().objects.values_list("email", "username")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(user_list, list(u.items() for u in res.data))
