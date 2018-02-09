from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from meets.models import Meet

class MeetsModelSerializer(serializers.ModelSerializer):
    user_fk = UserDisplaySerializer()
    class Meta:
        model = Meet
        fields = (
            'user_fk',
            'meet_name',
            'date',
            'time',
            'description',
            'meet_image',
            'users_joining',
        )
