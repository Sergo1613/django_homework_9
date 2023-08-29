from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная - смартфоны'
    }
    return render(request, 'main/home.html', context)


def categories(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Смартфоны - все модели'
    }
    return render(request, 'main/categories.html', context)


def product(request, pk):
    product_item = Product.objects.filter(pk=pk)
    context = {
        'object_list': product_item,
    }
    return render(request, 'main/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'main/contacts.html')
