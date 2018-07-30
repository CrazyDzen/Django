from django.shortcuts import render , get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView
from . import models
import categories


def index(request):
    category = get_list_or_404(categories.models.Category)
    product = get_list_or_404(models.Product)
    return render(request, 'products/index.html', {'product': product, 'category': category})


def category_list(request, pk):
    category = get_list_or_404(categories.models.Category)
    group = get_object_or_404(categories.models.Category, id=pk)
    product = get_list_or_404(models.Product, category_id=pk)
    return render(request, 'products/group.html', {'category': category, 'product': product, 'group': group})


def description(request, pk):
    category = get_list_or_404(categories.models.Category)
    product = get_object_or_404(models.Product, id=pk)
    return render(request, 'products/description.html', {'category': category, 'product': product})


def toys(request):
    category = get_list_or_404(categories.models.Category)
    product = get_list_or_404(models.Product)
    return render(request, 'products/products.html', {'product': product, 'category': category})

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['name', 'image', 'content', 'category', 'cost']

