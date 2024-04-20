from django.urls import path
from . import views




app_name = 'auth'
urlpatterns = [
    # path('emailsignup/', views.clsRegisterView.as_view(), name='register-view'), ##class view
    path('emailsignup/', views.RegisterView, name='register-view'), ##function view
    path('login/', views.LoginView, name='login-view')
]