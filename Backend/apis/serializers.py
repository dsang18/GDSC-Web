# apis/serializers.py
from rest_framework import serializers
from library_app.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ("title", "author", "ISBN")
        