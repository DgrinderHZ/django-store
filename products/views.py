from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import AddProductForm

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    params = {'products': products}
    return render(request, 'products/products-list.html', params)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-details.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = CreateView
    form_class = AddProductForm
    template_name = "products/product-add.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = AddProductForm
    template_name = "products/product-add.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('products_list')


class ProductDeleteView(DeleteView):
    model = Product

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('products_list')
