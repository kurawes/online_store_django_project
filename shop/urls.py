from django.urls import path
from . import views
from .views import ProductDetailView


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('shop/', views.shop_view, name='shop'),
    path('category_list/', views.category_view, name='category_list'),
    path('product_type_list/', views.product_type_view, name='product_type_list'),
    path('product_list/', views.product_view, name='product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
