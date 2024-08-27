from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializator, ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from .permissions import ProfilePermission
from rest_framework.exceptions import NotFound


class Register(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegistrationSerializator


class Profile(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (ProfilePermission, )

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            user = self.get_queryset().get(slug = slug)
            return user
        except get_user_model().DoesNotExist:
            raise NotFound(f"User with slug {slug} has not been found")
