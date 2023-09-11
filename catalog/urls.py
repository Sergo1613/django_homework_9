from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductListView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product')
]
