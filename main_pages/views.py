from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'main_pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


def terms_and_conditions(request):
    return render(request, 'main_pages/terms_and_conditions.html')
