from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from movie.models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = "movie/movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    success_url = reverse_lazy('movie:movie-list')
    fields = '__all__'


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    success_url = reverse_lazy('movie:movie-list')
    fields = '__all__'


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:movie-list')

