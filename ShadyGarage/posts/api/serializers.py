from rest_framework import serializers
from django.utils.timesince import timesince
from posts.models import Post
from accounts.api import serializers as accounts_serialisers
class PostModelSerializer(serializers.ModelSerializer):
    user_fk = accounts_serialisers.UserDisplaySerializer()
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'user_fk',
            'post_title',
            'post_image',
            'post_description',
            'post_likes',
            'post_created',
            'date_display',
            'timesince',
        )

    def get_date_display(self, obj):
        return obj.post_created.strftime("%b %d %I:%M %p ")

    def get_timesince(self, obj):
        return timesince(obj.post_created) + " siden"

    
