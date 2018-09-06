from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from django.db.models import Q
from carts.models import Cart
from .forms import CustomProductForm
from django.core.urlresolvers import reverse_lazy

class ProductList(ListView):
    template_name = "products/products_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductList, self).get_context_data(*args, **kwargs)


        cart_obj, created = Cart.objects.get_or_create(self.request)

        if not created:
            cart_obj = cart_obj

        context['cart_obj'] = cart_obj
        return context


    def get_queryset(self, *args, **kwargs):
        query = self.kwargs.get('category')
        if query == 'list':
            qs = Product.objects.all()
            return qs
        if query is not None:
            qs = Product.objects.filter(
                Q(category__icontains=query),
            )
        return qs

class ProductDetail(DetailView):
    template_name = "products/product_detail.html"
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(*args, **kwargs)

        cart_obj, created = Cart.objects.get_or_create(self.request)

        if not created:
            cart_obj = cart_obj
        context['cart_obj'] = cart_obj
        return context


class CustomSticker(LoginRequiredMixin, CreateView):
    template_name = "products/custom_sticker.html"
    form_class = CustomProductForm
    success_url = reverse_lazy("product:customsuccess", kwargs={'category':'success','slug':'c'})

    def form_valid(self, form):
        cs_form = form.save(commit = False)
        cs_form.user = self.request.user
        cs_form.save()
        return HttpResponseRedirect(reverse_lazy("products:customsuccess", kwargs={'category':'success','slug':'c'}))

class CustomStickerSuccess(TemplateView):
    template_name = "products/custom_product_success.html"
