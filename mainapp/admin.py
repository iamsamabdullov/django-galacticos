from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class PlayersAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Players
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "url",)
    list_display_links = ("name",)

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")

@admin.register(Players)
class PlayersAdmin(TranslationAdmin):
    list_display = ("name", "category", "url", "get_image")
    readonly_fields = ("get_image",)
    list_display_links = ("name",)
    list_filter = ("category", "year")
    search_field = ("name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    actions = ["publish", "unpublish"] 
    form = PlayersAdminForm
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')
    
    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

        
    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Изображение"

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "player", "id")
    readonly_fields = ("name", "email")

@admin.register(PlayersShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "player", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "player", "ip")
admin.site.register(RatingStar)



