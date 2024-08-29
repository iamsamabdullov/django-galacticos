from django.urls import path

from . import views

urlpatterns = [
    path("", views.PlayersView.as_view()),
    path("filter/", views.FilterPlayersView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.PlayerDetailView.as_view(), name="player_detail"),
    path('review/<int:pk>/', views.AddReview.as_view(),name="add_review"),
]
