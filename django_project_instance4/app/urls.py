from django.urls import path

from . import views

urlpatterns = [
    path('get_books/', views.GetBooksView.as_view(), name='get_books'),
]
