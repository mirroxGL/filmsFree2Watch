from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator


def index(request):
    search_query = request.GET.get("search", '')

    if search_query:
        films = Film.objects.filter(title__icontains=search_query)
    else:
        films = Film.objects.all()

    paginator = Paginator(films, 10)

    return render(request, 'main/index.html', {"films": films})



class FilmDetailView(DetailView):
    model = Film
    template_name = 'main/details_view.html'
    context_object_name = 'article'

class FilmUpdateView(UpdateView):
    model = Film
    template_name = 'main/edit_film.html'
    success_url = '/'
    form_class = FilmForm

class FilmDeleteView(DeleteView):
    model = Film
    success_url = '/'
    template_name = 'main/delete_film.html'


def create(request):
    error = ''
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Form is not valid'

    form = FilmForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


