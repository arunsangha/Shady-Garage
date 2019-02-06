from rest_framework import serializers
from blogs.models import Blog, Car
from django.urls import reverse

class BlogListSerializer(serializers.ModelSerializer):

    car = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'title',
            'image',
            'url',
            'car',
            'height',
        )

    def get_car(self, obj):
        return "{}".format(obj.car.make)

    def get_url(self, obj):
        return reverse("blogs:detail", kwargs={'slug':obj.slug})

    def get_image(self, obj):
        return obj.top_image.url

    def get_height(self, obj):
        from random import randint
        return randint(320, 500)
