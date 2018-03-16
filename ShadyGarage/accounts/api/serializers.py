from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from accounts.models import Profile

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'id',
        ]

class ProfileDisplaySerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Profile
        fields = (
            'user',
            'profile_pic',
            'teams'
            'age',
            'thumbnail',
        )
