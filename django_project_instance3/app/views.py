from typing import List, Optional, Union
import json

from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers
from .cache_manager import __cache_manager__


class GetBooksView(APIView):
    @staticmethod
    def _get_non_cached_titles(all_titles: List[str], cache: List[Optional[bytes]]) -> List[str]:
        non_cached_titles: List[str] = []
        for title, cached_result in zip(all_titles, cache):
            if cached_result is None:
                non_cached_titles.append(title)
        return non_cached_titles

    def get(self, request):
        book_titles = request.data['book_titles']

        from_cache: List[Union[bytes, None]] = __cache_manager__.get_cache(book_titles=book_titles)
        non_cached_titles = self._get_non_cached_titles(all_titles=book_titles, cache=from_cache)

        from_cache_without_none: List[dict] = []
        for cache in filter(lambda x: x is not None, from_cache):
            from_cache_without_none.append(json.loads(cache))

        if not non_cached_titles:
            return Response({'ANSWER': from_cache_without_none})

        book_qs = models.Book.objects \
            .filter(title__in=non_cached_titles) \
            .select_related('author') \
            .only('title', 'author', 'author__name')

        books_to_add_to_cache = {}

        # В общем случае количество записей, которое запрашивает пользователь = 3
        # При таком варианте разница во времени между итераций и по отдельности сериализации
        # минимальна по сравнению с сериализацию булком (через many = True)
        serializer_data = []
        for book in book_qs:
            data = serializers.BookSerializer(book).data
            books_to_add_to_cache[book.title] = json.dumps(data)
            serializer_data.append(data)

        __cache_manager__.set_cache(books_to_add_to_cache)

        return Response({'ANSWER': serializer_data})
