from django.urls import path
from .views import (ProductListView,ProductDetailView,
                   ProductCreateView,ProductDeleteView,
                   get_product_info)


urlpatterns = [
        path('home/', ProductListView.as_view(), name='home'),
        path('<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
        path('<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),
        path('new/', ProductCreateView.as_view(), name='product_new'),
        path('consume/',get_product_info)
]

