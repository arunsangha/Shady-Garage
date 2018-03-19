from rest_framework import serializers, reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from django.urls import reverse
from accounts.models import Profile
from accounts.models import User as model_user
class ProfileDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'profile_pic',
            'teams',
            'age',
            'thumbnail',
        )

class UserDisplaySerializer(serializers.ModelSerializer):
    profile = ProfileDisplaySerializer()
    url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'id',
            'profile',
            'url',
        ]

    def get_url(self, obj):
        return reverse("accounts:profile_page_pk", kwargs={'pk':obj.id})
