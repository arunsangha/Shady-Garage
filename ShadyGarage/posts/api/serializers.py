from rest_framework import serializers
from django.utils.timesince import timesince
from posts.models import Post, PostComment, Notification, PostCommentReply
from accounts.api import serializers as accounts_serialisers
from django.urls import reverse
from accounts import models as accounts_models
from django.shortcuts import get_object_or_404

class PostModelSerializer(serializers.ModelSerializer):
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    post_likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    comment_url = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    activity_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'user_fk',
            'post_title',
            'post_image',
            'thumbnail',
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
            'activity_count',
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

    def get_activity_count(self, obj):
        qs = Notification.objects.filter(owner=obj.user_fk).exclude(user_fk=obj.user_fk)
        count_ = qs.filter(seen=False).count()
        return count_


class PostCommentSerializer(serializers.ModelSerializer):
    post_fk = PostModelSerializer(read_only=True)
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    profile = accounts_serialisers.ProfileDisplaySerializer(read_only=True)
    comment_replys = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    class Meta:
        model = PostComment
        fields= (
            'post_fk',
            'user_fk',
            'profile',
            'comment',
            'created',
            'id',
            'comment_replys',
        )

    def get_comment_replys(self, obj):
        replys_ = PostCommentReply.objects.filter(comment_fk=obj.id).count()
        if(replys_):
            return replys_
        return 0

    def get_created(self, obj):
        return timesince(obj.created)

class PostCommentReplySerializer(serializers.ModelSerializer):
    comment_fk = PostCommentSerializer(read_only=True)
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = PostCommentReply
        fields=(
            'comment_fk',
            'user_fk',
            'comment',
            'timesince',
        )

    def get_timesince(self, obj):
        return timesince(obj.created)

class PostCommentReplyDetailSerializer(serializers.ModelSerializer):
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = PostCommentReply
        fields=(
            'user_fk',
            'comment',
            'timesince',
        )

    def get_timesince(self, obj):
        return timesince(obj.created)

class NotificationSerializer(serializers.ModelSerializer):
    post_fk = PostModelSerializer(read_only=True)
    user_fk = accounts_serialisers.UserDisplaySerializer(read_only=True)
    owner = accounts_serialisers.UserDisplaySerializer(read_only=True)
    noti_fk = PostCommentSerializer(read_only=True)
    timesince = serializers.SerializerMethodField()
    did_mark_seen = serializers.SerializerMethodField()
    noti_reply_fk = PostCommentReplySerializer(read_only=True)
    class Meta:
        model = Notification
        fields = (
            'id',
            'post_fk',
            'user_fk',
            'noti_fk',
            'owner',
            'commented',
            'liked',
            'timesince',
            'seen',
            'did_mark_seen',
            'noti_reply_fk',
        )

    def get_timesince(self, obj):
        return timesince(obj.created)

    def get_did_mark_seen(self, obj):
        if obj.seen == True:
            return True
        return False


class NotificationSeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id',
            'seen',
        )

class PostCreateSerializer(serializers.ModelSerializer):
    post_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Post
        fields = (
            'post_title',
            'post_description',
            'post_image',
        )
