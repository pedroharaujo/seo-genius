from django.urls import path
from . import views

app_name = 'main_pages'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('terms-and-conditions/', views.terms_and_conditions,
         name='terms_and_conditions'),
]
