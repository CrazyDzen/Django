from django.shortcuts import render
from . import models


def index(request):
    query = models.Product.objects.all()
    return render(request, 'products/index.html', {'query': query})


