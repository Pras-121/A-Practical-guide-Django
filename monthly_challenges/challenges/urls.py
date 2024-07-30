from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_season_int),
    path("<str:month>", views.monthly_season,name="monthly_seasons")
]

