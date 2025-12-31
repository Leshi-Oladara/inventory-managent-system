from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Order
from .forms import ProductForm, CategoryForm, OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    orders = Order.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'orders': orders,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'dashboard/products.html', context)

@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:products')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_add.html', context)

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard:products')
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard:products')
    context = {
        'product': product,
    }
    return render(request, 'dashboard/product_delete.html', context)

@login_required
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'dashboard/categories.html', context)

@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/category_add.html', context)

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:categories')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/category_edit.html', context)

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('dashboard:categories')
    context = {
        'category': category,
    }
    return render(request, 'dashboard/category_delete.html', context)

@login_required
def orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'dashboard/orders.html', context)

@login_required
def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.staff = request.user
            order.save()
            return redirect('dashboard:orders')
    else:
        form = OrderForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/order_add.html', context)
