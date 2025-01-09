from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView, DetailView


class HomeView(TemplateView):
    template_name = 'main_pages/home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('users:dashboard'))
        return super().dispatch(request, *args, **kwargs)


def terms_and_conditions(request):
    return render(request, 'main_pages/terms_and_conditions.html')
