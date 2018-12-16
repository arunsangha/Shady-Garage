from django.shortcuts import render, redirect
from .models import ObjectViewed
from django.http import JsonResponse, Http404
# Create your views here.

def get_views(request):
    if request.is_ajax() and request.method == 'GET':
        id = request.GET.get('id')
        object_class = request.GET.get('object_class')


        if id and object_class:
            #Add other classes you wish to use for getting views count
            object_types = {
             'Blog':30,
            }

            qs = ObjectViewed.objects.filter(object_id=id, content_type=object_types[object_class])
            views = qs.count()
    
            return JsonResponse({'status':'success', 'views':views})

        return JsonResponse({'status':'false', 'message':'No id or object class found'})

    return redirect("blogs:blogs_list")
