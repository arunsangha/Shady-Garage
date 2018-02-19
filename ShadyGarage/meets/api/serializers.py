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
    joining = serializers.SerializerMethodField()
    did_join = serializers.SerializerMethodField()

    class Meta:
        model = Meet
        fields = (
            'user_fk',
            'meet_name',
            'date',
            'time',
            'description',
            'meet_image',
            'joining',
            'day',
            'url',
            'did_join',
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

    def get_joining(self, obj):
        return obj.users_joining.all().count()

    def get_did_join(self, obj):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated():
            if user in obj.users_joining.all():
                return True
        return False 
