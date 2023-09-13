from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductCreateView, ContactsView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

]
