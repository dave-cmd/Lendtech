from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('payments/', views.payments, name='payments'),
    path('loans/', views.loans, name='loans'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('register_page', views.register_page, name='register_page'),
]