from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('products/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm, template_name='registration/login.html'), name='login'),
] 