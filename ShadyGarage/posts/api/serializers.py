from rest_framework import serializers
from django.utils.timesince import timesince
from posts.models import Post
from accounts.api import serializers as accounts_serialisers
from django.urls import reverse

class PostModelSerializer(serializers.ModelSerializer):
    user_fk = accounts_serialisers.UserDisplaySerializer()
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    post_likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
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
            'url',
            'did_like',
        )

    def get_date_display(self, obj):
        return obj.post_created.strftime("%b %d %I:%M %p ")

    def get_timesince(self, obj):
        return timesince(obj.post_created) + " siden"

    def get_url(self, obj):
        return reverse("posts:post_detail", kwargs={'slug':obj.slug})

    def get_post_likes(self, obj):
        return obj.post_likes.all().count()

    def get_did_like(self, obj):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated():
            if user in obj.post_likes.all():
                return True
        return False
