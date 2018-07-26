from django.shortcuts import render, get_list_or_404
from . import models
import categories


def index(request):
    product = models.Product.objects.all()
    category = categories.models.Category.objects.all()
    return render(request, 'products/index.html', {'product': product, 'category': category})
