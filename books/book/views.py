from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView
from .models import Booklist
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Bookview(CreateView):
    model = Booklist
    fields = ['name', 'price', 'pages', 'author']
    template_name = 'book/media.html'

class Booklists(ListView):
    model = Booklist
    template_name = 'book/media2.html'

class BookDelete(DeleteView):
    model = Booklist
    template_name = 'book/delete.html'
    success_url = reverse_lazy('booklist')

class BookUpdate(UpdateView):
    model = Booklist
    fields = ['name', 'price', 'pages', 'author']
    template_name = 'book/update.html'

class Sort(ListView):
    model = Booklist
    paginate_by = 50
    template_name = 'book/media2.html'

    ordering = ['-price']

class Sort2(ListView):
    model = Booklist
    paginate_by = 2
    context_object_name = 'books'
    template_name = 'book/media2.html'

    ordering = ['-pages']

    def get_queryset(self):
        try:
            name = self.request.GET['data']
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(name__startswith=name)
        else:
            object_list = self.model.objects.all()
        return object_list

class Search(ListView):
    template_name = 'book/media2.html'
    model = Booklist

    def get_queryset(self):
        try:
            name = self.kwargs['data']
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(name__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list