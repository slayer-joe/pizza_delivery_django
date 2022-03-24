from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect("register")),
    path('logout/', views.logout, name="logout_page"),
    # path('users/', views.UsersView.as_view(), name="all_list"),
    path('login/', views.LoginView.as_view(), name='user_login_page'),
    path('register/', views.RegisterView.as_view(), name="register")
]