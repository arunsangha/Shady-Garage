from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView
)
from .models import Product
from django.db.models import Q

class ProductList(ListView):
    template_name = "products/products_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductList, self).get_context_data(*args, **kwargs)
        return context


    def get_queryset(self, *args, **kwargs):
        query = self.kwargs.get('category')
        print(query)
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
