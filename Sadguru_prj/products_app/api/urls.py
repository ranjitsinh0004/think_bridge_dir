from rest_framework import routers
from products_app.api import views
from rest_framework.routers import DefaultRouter
from django.urls import path,include
router= DefaultRouter()
router.register('productinfo',views.ProductCRUDCBV,)

urlpatterns = [
                path('',include(router.urls)),
]