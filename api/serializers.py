from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'first_name',
			'last_name',
			'email',
			'avatar',
			'phone_number',
			'dob',
			'role',
			'groups',
		]