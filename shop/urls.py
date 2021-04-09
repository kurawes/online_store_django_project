from django.urls import path
from . import views
from .views import CategoryUpdateView, CategoryDeleteView, CategoryCreateView


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('shop/', views.shop_view, name='shop'),
    path('category_list/', views.category_view, name='category_list'),
    path('product_type_list/', views.product_type_view, name='product_type_list'),
    path('cat_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('cat_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('cat_create/', CategoryCreateView.as_view(), name='category_create'),
]
