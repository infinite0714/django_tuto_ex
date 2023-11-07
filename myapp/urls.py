from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("morning/", views.morning, name="morning"),
    path("article/<int:articleID>/", views.article, name="article"),
    path("articles/<int:month>/<int:year>", views.articles, name="articles"),
    path("sendemail/<str:emailto>", views.sendSimpleEmail, name="sendemail")
]