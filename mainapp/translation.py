from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Players)
class PlayersTranslationOptions(TranslationOptions):
    fields = ('name', 'tagline', 'description', 'country')