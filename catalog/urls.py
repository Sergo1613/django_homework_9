from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, categories, category_smartphone

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/smartphone/', category_smartphone, name='category_smartphone')
]
