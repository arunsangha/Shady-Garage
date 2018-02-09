from rest_framework import serializers
from posts.models import Post

class PostModelSerializer(serializers.ModelSerializer):
    #user = ProfileDisplaySerializer()
    class Meta:
        model = Post
        fields = (
            'post_title',
            'user_fk',
            'post_image',
            'post_description',
            'post_likes',
            'post_created',
        )
