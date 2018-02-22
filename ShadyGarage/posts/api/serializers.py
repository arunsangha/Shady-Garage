from rest_framework import serializers
from django.utils.timesince import timesince
from posts.models import Post, PostComment
from accounts.api import serializers as accounts_serialisers
from django.urls import reverse

class PostModelSerializer(serializers.ModelSerializer):
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    post_likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    comment_url = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
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
            'id',
            'comment_url',
            'comment_count',
            'slug',
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

    def get_comment_url(self, obj):
        return reverse("posts:post_comment", kwargs={'slug':obj.slug})

    def get_comment_count(self, obj):
        return obj.post_comment_fk.count()

class PostCommentSerializer(serializers.ModelSerializer):
    post_fk = PostModelSerializer(read_only=True)
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    class Meta:
        model = PostComment
        fields= (
            'post_fk',
            'user_fk',
            'comment',
            'created',
        )
