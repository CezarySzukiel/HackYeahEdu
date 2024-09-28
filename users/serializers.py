from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer

from .models import CustomUser


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'first_name', 'last_name',)
        read_only_fields = ('pk',)
