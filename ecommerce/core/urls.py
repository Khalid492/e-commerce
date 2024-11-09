from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name='core'
urlpatterns=[
    path('',views.index,name='index'),
    path('contact-us',views.contact_us,name='contact_us'),
    path('signup',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
]   