from categories.models import Category
from categories.forms import AddCategoryForm
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.
def category_add(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('category_list')
        else:
            form = AddCategoryForm()
        return render(request, 'categories/category_add.html', {'form': form})
    else:
        return redirect('products_list')


def category_list(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(request, 'categories/category_list.html', ctx)


def category_edit(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            form = AddCategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('category_list')
        else:
            form = AddCategoryForm(instance=category)
        return render(request, 'categories/category_add.html', {'form': form})
    else:
        return redirect('products_list')
