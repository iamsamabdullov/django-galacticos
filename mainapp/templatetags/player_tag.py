from django import template
from mainapp.models import Category, Players

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('players/tags/last_players.html')
def get_last_players(count=3):
    players = Players.objects.order_by("id")[:count]
    return{"last_players":players}