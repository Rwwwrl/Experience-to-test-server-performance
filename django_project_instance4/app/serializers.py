from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = models.Book
        fields = ['author', 'title']
