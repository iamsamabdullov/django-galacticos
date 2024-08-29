from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm, RatingForm
from .models import *
from django.http import JsonResponse, HttpResponse

class Categorys:
    def get_category(self):
        return Category.objects.all()

class PlayersView(Categorys,ListView):
    model = Players
    qureyset = Players.objects.filter(draft=False)
    paginate_by = 3

    

class PlayerDetailView(Categorys, DetailView):
    model = Players
    slug_field = 'url'
    def get(self, request, slug):
        player = Players.objects.get(url=slug)
        star_form = RatingForm()
        form = ReviewForm()
        return render(request, 'players/player_detail.html', {"player":player, "star_form":star_form, "form": form})
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['star_form'] = RatingForm()
        context["form"] = ReviewForm()
        return context
    

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        player = Players.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.player = player
            form.save()
        return redirect(player.get_absolute_url())
    
class FilterPlayersView(Category, ListView):
    def get_queryset(self):
        queryset = Players.objects.filter(category__in=self.request.GET.getlist('category'))
        return queryset
    
class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                player_id=int(request.POST.get("player")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    """Поиск"""
    paginate_by = 3

    def get_queryset(self):
        return Players.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context