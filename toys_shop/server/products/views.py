from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models
from . import forms


'''
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
    return render(request, 'products/description.html', {'category': category, 'product': product})
    '''


class ProductCreate(PermissionRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products:product')
    template_name = 'products/edit.html'
    permission_required = 'categories.category.Can add category'
    login_url = reverse_lazy('categories:list')


class ProductList(PermissionRequiredMixin, ListView):
    context_object_name = 'query'
    template_name = 'products/product_edit.html'
    queryset = get_list_or_404(models.Product)
    permission_required = 'categories.category.Can add category'
    login_url = reverse_lazy('categories:list')
    paginate_by = 8


class ProductsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = forms.ProductForm
    model = models.Product
    success_url = reverse_lazy('products:product')
    template_name = 'products/update.html'
    permission_required = 'categories.category.Can_add_category'
    login_url = reverse_lazy('categories:list')


class ProductsDelete(PermissionRequiredMixin, DeleteView):
    context_object_name = 'query'
    form_class = forms.ProductForm
    model = models.Product
    success_url = reverse_lazy('products:product')
    template_name = 'products/delete.html'
    permission_required = 'categories.category.Can add category'
    login_url = reverse_lazy('categories:list')
