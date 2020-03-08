from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.user_page, name="user-page"),
    path('account/', views.account_settings, name="account"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('create_order/<str:pk>', views.create_order, name='create_order'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order')

]
