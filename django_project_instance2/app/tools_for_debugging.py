from typing import Callable
from datetime import datetime


def time_it(func: Callable):
    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(end - start)
        return result

    return inner
