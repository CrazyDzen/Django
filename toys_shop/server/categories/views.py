from django.shortcuts import render, get_list_or_404, get_object_or_404
from products import models


def category_name(request):
    category = set([el.category for el in get_list_or_404(models.Product)])
    return render(request, 'categories/index.html', {'category': category})


def group(request, pk):
    category = set([el.category for el in get_list_or_404(models.Product)])
    group = get_list_or_404(models.Product, category_id=pk)[0].category
    return render(request, 'categories/group.html', {'category': category, 'group': group})


def description(request, pk):
    category = set([el.category for el in get_list_or_404(models.Product)])
    return render(request, 'categories/description.html', {'category': category, 'pk': pk})
