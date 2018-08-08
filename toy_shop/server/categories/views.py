from django.shortcuts import render, get_list_or_404, get_object_or_404
from products import models


def category_name(request):
    category = set([el.category for el in get_list_or_404(models.Product)])
    return render(request, 'categories/index.html', {'category': category})
