from rest_framework import serializers, reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from django.urls import reverse
from accounts.models import Profile
from accounts.models import User as model_user

from rest_framework.serializers import ValidationError

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

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

        extra_kwargs = {"password":
                        {"write_only":True}
                       }


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'token',
        )

        extra_kwargs = {"password":
                        {"write_only":True}
                    }

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data.get("password", None)
        if not username:
            raise ValidationError("A username must be required to login.")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None:
            user_obj = user
        else:
            raise ValidationError("This username is not valid!")


        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again!")


        data["token"] = "SOME RANDOM TOKEN"

        return data
