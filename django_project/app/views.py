from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response

from . import consts, models, serializers


class GetBooksView(APIView):
    def get(self, request):
        books = models.Book.objects.select_related('author').all()
        serializer = serializers.BookSerializer(books, many=True)
        now = timezone.now().strftime(consts.TIME_FORMAT)
        return Response({'ANSWER': serializer.data, 'date_time': now})
