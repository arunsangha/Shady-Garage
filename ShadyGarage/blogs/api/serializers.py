from rest_framework import serializers
from blogs.models import Blog, Car
from django.urls import reverse

class BlogListSerializer(serializers.ModelSerializer):

    car = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'title',
            'top_image',
            'car',
            'url',
        )

    def get_car(self, obj):
        return "{} {}".format(obj.car.make, obj.car.model)

    def get_url(self, obj):
        return obj.get_absolute_url
