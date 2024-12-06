from django.urls import path
from . import views

app_name = 'main_pages'

urlpatterns = [
    path('terms-and-conditions/', views.terms_and_conditions,
         name='terms_and_conditions'),
]
