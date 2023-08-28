from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.

def index(request):
    context = {
        'object_list': Category.objects.all()[:2],
        'title': 'Главная - смартфоны'
    }
    return render(request, 'main/home.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Смартфоны - все модели'
    }
    return render(request, 'main/categories.html', context)


def category_smartphone(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f"Смартфоны - модели {category_item.name}"
    }
    return render(request, 'main/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'main/contacts.html')
