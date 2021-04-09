from django.urls import path
from . import views
from .views import CategoryUpdateView, CategoryDeleteView, CategoryCreateView,PTDeleteView, PTUpdateView,\
    PTCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('shop/', views.shop_view, name='shop'),
    path('category_list/', views.category_view, name='category_list'),
    path('cat_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('cat_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('cat_create/', CategoryCreateView.as_view(), name='category_create'),
    path('product_type_list/', views.product_type_view, name='product_type_list'),
    path('pt_update/<int:pk>', PTUpdateView.as_view(), name='product_type_update'),
    path('pt_delete/<int:pk>', PTDeleteView.as_view(), name='product_type_delete'),
    path('pt_create/', PTCreateView.as_view(), name='product_type_create'),
    path('product_list/', views.product_view, name='product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
]
