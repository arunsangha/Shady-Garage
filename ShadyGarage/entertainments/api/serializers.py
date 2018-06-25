from rest_framework import serializers
from entertainments.models import Entertainment

class EntertainmentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    did_like = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    class Meta:
        model = Entertainment
        fields = (
            'id',
            'title',
            'image',
            'youtube_link',
            'created',
            'likes',
            'did_like',
        )


    def get_likes(self, obj):
        return obj.likes.all().count()

    def get_did_like(self, obj):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                return True
        return False

    def get_id(self, obj):
        return obj.id
