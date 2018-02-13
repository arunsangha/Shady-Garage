from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from meets.models import Meet
from django.urls import reverse

class MeetsModelSerializer(serializers.ModelSerializer):
    user_fk = UserDisplaySerializer()
    day = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
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
            'url',
        )

    def get_day(self, obj):

        days = (
            'Mandag',
            'Tirsdag',
            'Onsdag',
            'Torsdag',
            'Fredag',
            'Lørdag',
            'Søndag',
        )

        return days[obj.date.weekday()]

    def get_date(self, obj):
        return obj.date.strftime("%Y.%m.%d")

    def get_time(self, obj):
        return obj.time.strftime("%H:%M")

    def get_url(self, obj):
        return reverse("meets:single", kwargs={'slug':obj.slug})
