from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers


class GetBooksView(APIView):
    def get(self, request):
        try:
            book_titles = request.data['book_titles']
        except KeyError:
            book_qs = models.Book.objects.all()
        else:
            book_qs = models.Book.objects.filter(title__in=book_titles)

        books_qs = book_qs.select_related('author').only('title', 'author', 'author__name')
        serializer = serializers.BookSerializer(books_qs, many=True)
        return Response({'ANSWER': serializer.data})
