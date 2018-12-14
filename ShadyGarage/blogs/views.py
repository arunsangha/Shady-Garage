from django.shortcuts import render, redirect
from .models import Blog, Car, UserVote
from django.views.generic import DetailView, ListView
from django.http import Http404
from django.http import JsonResponse
from analytics.signals import object_viewed_signal

class BlogDetail(DetailView):
    template_name = "blogs/blogs_detail.html"
    model = Blog


    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            object = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise Http404("Not found..")

        object_viewed_signal.send(sender=object.__class__, instance=object, request=request)
        return object

class BlogList(ListView):
    template_name = "blogs/blogs_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Blog.objects.all()
        return qs

def user_vote(request):
     if request.is_ajax():
         car_id = request.POST.get('id')
         vote = request.POST.get('vote')

         try:
            car_obj = Car.objects.get(pk=car_id)
         except Car.DoesNotExist:
            response = {'status':'false','message':'Error getting car'}


         vote_obj = UserVote.objects.create(car=car_obj,vote=vote)

         print(vote_obj)

         response = {'status':'success','message':'NiceWork'}

         vote_true_count = UserVote.objects.filter(car=car_obj, vote=True).count()
         vote_count = UserVote.objects.all().count()
         print(vote_true_count)
         print(vote_count)
         voted_true = round((vote_true_count/vote_count) * 100)
         voted_false = round(((vote_count - vote_true_count)/vote_count) * 100)
         response = {'status':'success','message':'NiceWork', 'voted_true':voted_true, 'voted_false':voted_false}

         return JsonResponse(response, status=200)
     redirect("blogs:list")
