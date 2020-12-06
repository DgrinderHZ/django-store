from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView
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



def product_edit(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)

        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return render(request, "products/product-added.html")
        else:
            form = AddProductForm(instance=product)
        return render(request, "products/product-add.html", {'form': form})
    else:
        return redirect('products_list')


def product_delete(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        get_object_or_404(Product, pk=pk).delete()
        return render(request, "products/product-deleted.html")
    else:
        return redirect('products_list')
