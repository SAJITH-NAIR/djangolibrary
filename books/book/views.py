from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Choice


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Bookview(CreateView):
    model = Choice
    fields = ['name', 'price']
    template_name = 'book/media.html'

class Booklist(ListView):
    model = Choice
    template_name = 'book/media2.html'

class AboutView(TemplateView):
    template_name = "index.html"