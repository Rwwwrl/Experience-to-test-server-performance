import redis
from typing import Iterable, Dict


class RedisCacheManager:

    _instance: 'RedisCacheManager' = None

    def __new__(cls):
        if cls._instance:
            return cls._instance
        instance = super().__new__(cls)
        client = redis.Redis(host='redis_cache', port=6379)
        instance._client = client
        cls._instance = instance
        return instance

    @property
    def client(self) -> redis.Redis:
        return self._client

    def get_cache(self, book_titles: Iterable[str]) -> Iterable[dict]:
        return self.client.mget(book_titles)

    def set_cache(self, book_title_to_data: Dict[str, Dict]) -> dict:
        self.client.mset(book_title_to_data)


__cache_manager__ = RedisCacheManager()