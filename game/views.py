from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from game.models import Game

class GameListView(ListView):
    model = Game
    template_name = "game/game_list.html"


class GameDetailView(DetailView):
    model = Game
    template_name = "game/game_detail.html"


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    success_url = reverse_lazy('game:game-list')
    fields = '__all__'


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    success_url = reverse_lazy('game:game-list')
    fields = '__all__'


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('game:game-list')

