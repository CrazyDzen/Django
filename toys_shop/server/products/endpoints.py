import json
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from . import models


def api_product_list(request, page):
    query = get_list_or_404(models.Product)
    paginator = Paginator(query, 6)
    query_page = paginator.get_page(page)
    data = map(lambda itm: {
        'id': itm.id,
        'name': itm.name,
        'image': itm.image.name,
        'cost': float(itm.cost)
    }, query_page)
    context = json.dumps({'results': list(data)})
    return HttpResponse(context)


def api_product_cat(request, pk):
    query = get_list_or_404(models.Product, category_id=pk)
    data = map(lambda itm: {
        'id': itm.id,
        'name': itm.name,
        'image': itm.image.name,
        'cost': float(itm.cost)
    }, query)
    context = json.dumps({'results': list(data)})
    return HttpResponse(context)


def api_product(request, pk):
    query = get_list_or_404(models.Product, id=pk)
    data = map(lambda itm: {
        'id': itm.id,
        'category_id': itm.category.id,
        'category_name': itm.category.name,
        'name': itm.name,
        'image': itm.image.name,
        'content': itm.content,
        'cost': float(itm.cost)
    }, query)
    context = json.dumps({'results': list(data)})
    return HttpResponse(context)
