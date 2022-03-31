from django.contrib.auth import get_user_model

from rest_framework import generics, mixins

from .serializers import UserSerializer

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer