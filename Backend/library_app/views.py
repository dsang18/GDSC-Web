from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class BookListView(ListView):
    model = Books
    template_name = "books_list.html"

