from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer

from .models import CustomUser


class CustomUserDetailSerializer(UserDetailsSerializer):
    pass

# class UserDetailsSerializer(UserDetailsSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'teacher')
#         read_only_fields = ('pk',)
