from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from meets.models import Meet, Meet_Comment
from django.urls import reverse
from django.utils.timesince import timesince
import json
from django.utils import timezone

class DateTimeFieldWihTZ(serializers.DateTimeField):
    '''Class to make output of a DateTime Field timezone aware
    '''
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)

class MeetsModelSerializer(serializers.ModelSerializer):
    user_fk = UserDisplaySerializer()
    day = serializers.SerializerMethodField()
    date = DateTimeFieldWihTZ(format='%d-%m-%Y')
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
            'category',
            'joining',
            'day',
            'url',
            'did_join',
            'location',
            'marker_image',
            'anonymous',
            'organizer',
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

        day = obj.date.weekday() + 1
        if day > 6:
            day = 0
        
        return days[day]

    def get_date(self, obj):
        return obj.date

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

class MeetCommentSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    meet_fk = MeetsModelSerializer()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Meet_Comment
        fields = (
            'user',
            'meet_fk',
            'comment',
            'created',
        )

    def get_created(self, obj):
        return timesince(obj.created)
