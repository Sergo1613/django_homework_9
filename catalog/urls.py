from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, categories, product, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', categories, name='categories'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/smartphone/', product, name='product')
]
