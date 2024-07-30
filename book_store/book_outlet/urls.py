from django.urls import path
from . import views
urlpatterns =[
    path("",views.index, name='index-page'),
    path("<slug:slug>",views.book_detail, name="Book-Details-page")
]