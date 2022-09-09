# apis/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path("", getData, name="book_list"),
    path("add/", loadData, name="New Book")
]