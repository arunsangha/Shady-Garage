from django.contrib import admin
from .models import Car,Blog, UserVote
# Register your models here.
admin.site.register(Car)
admin.site.register(Blog)
admin.site.register(UserVote)
