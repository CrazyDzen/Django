from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms


def category_name():
    category = set([el.category for el in get_list_or_404(models.Product)])
    return category


def products_list(request):
    category = category_name()
    product = get_list_or_404(models.Product)
    return render(request, 'products/index.html', {'product': product, 'category': category})


def category_list(request, pk):
    category = category_name()
    product = get_list_or_404(models.Product, category_id=pk)
    group = product[0].category
    return render(request, 'products/group.html', {'category': category, 'product': product, 'group': group})


def description(request, pk):
    category = category_name()
    product = get_object_or_404(models.Product, id=pk)
    return render(request, 'products/description.html', {'category': category, 'product': product})


def toys(request):
    category = category_name()
    product = get_list_or_404(models.Product)
    return render(request, 'products/products.html', {'product': product, 'category': category})


class ProductCreate(CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('product')
    template_name = 'products/edit.html'


class ProductList(ListView):
    context_object_name = 'query'
    template_name = 'products/product_edit.html'
    queryset = get_list_or_404(models.Product)


class ProductsUpdate(UpdateView):
    form_class = forms.ProductForm
    model = models.Product
    success_url = reverse_lazy('product')
    template_name = 'products/update.html'


class ProductsDelete(DeleteView):
    context_object_name = 'query'
    form_class = forms.ProductForm
    model = models.Product
    success_url = reverse_lazy('product')
    template_name = 'products/delete.html'
