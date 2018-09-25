from django.urls import path
from one_app.views import ListNews, OneNew

urlpatterns = [
    path('', ListNews.as_view()),
    path('single/<int:pk>/', OneNew.as_view(), name="single"),
]
