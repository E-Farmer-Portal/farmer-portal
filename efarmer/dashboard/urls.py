from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('login/dashboard/', views.dashboard, name='dashboard'),
    path('login/dashboard/profile/', views.profile, name='profile'),
    path('login/dashboard/detail/', views.detail, name='detail'),
    path('login/dashboard/store/', views.store, name='store'),
    path('login/dashboard/cart/', views.cart, name='cart'),
    path('login/dashboard/cart/checkout/', views.checkout, name='checkout'),
    path('login/dashboard/update_item/', views.updateItem, name="update_item"),
    path('login/dashboard/process_order/', views.processOrder, name="process_order"),

]

