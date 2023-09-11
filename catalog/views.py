from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from catalog.models import Product


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная - смартфоны'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


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


class ContactsView(View):
    template_name = 'main/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
        return render(request, self.template_name)


