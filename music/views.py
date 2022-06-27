from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from music.models import Music

class MusicListView(ListView):
    model = Music
    template_name = "music/music_list.html"


class MusicDetailView(DetailView):
    model = Music
    template_name = "music/music_detail.html"


class MusicCreateView(LoginRequiredMixin, CreateView):
    model = Music
    success_url = reverse_lazy('music:music-list')
    fields = '__all__'


class MusicUpdateView(LoginRequiredMixin, UpdateView):
    model = Music
    success_url = reverse_lazy('music:music-list')
    fields = '__all__'


class MusicDeleteView(LoginRequiredMixin, DeleteView):
    model = Music
    success_url = reverse_lazy('music:music-list')

