from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Players(models.Model):
    name = models.CharField("Имя", max_length=100)
    number = models.IntegerField("Номер")
    position = models.CharField("Амплуа", max_length=100)
    games = models.IntegerField("Игры")
    goals = models.IntegerField("Голы")
    tagline = models.CharField("Прозвище", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="players/")
    year = models.PositiveSmallIntegerField("Дата рождения")
    country = models.CharField("Страна", max_length=30)
    datas = models.CharField("Годы выступления",max_length=30)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("player_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

class PlayersShots(models.Model):
    """Фото игроков"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="players_shots/")
    player = models.ForeignKey(Players, verbose_name="Игрок", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото игрока"
        verbose_name_plural = "Фото игрока"

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]

class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    player = models.ForeignKey(Players, on_delete=models.CASCADE, verbose_name="игрок", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.player}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    player = models.ForeignKey(Players, verbose_name="игрок", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.player}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"