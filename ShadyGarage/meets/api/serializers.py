from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from meets.models import Meet


class MeetsModelSerializer(serializers.ModelSerializer):
    user_fk = UserDisplaySerializer()
    day = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
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
            'day',
        )

    def get_day(self, obj):
        return obj.date.strftime("%A")

    def get_date(self, obj):
        return obj.date.strftime("%Y.%m.%d")

    def get_time(self, obj):
        return obj.time.strftime("%H:%M")
