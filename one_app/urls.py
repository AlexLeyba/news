from django.urls import path
from one_app.views import ListNews, OneNew, Like, Category_View, Search_View

urlpatterns = [
    path('', ListNews.as_view()),
    path('single/<int:pk>/', OneNew.as_view(), name="single"),
    path('single/<int:pk>/<int:post_pk>/', Like.as_view(), name="like_comment"),
    path('category/<slug:category_slug>', Category_View.as_view(), name="category"),
    path('search/', Search_View.as_view(), name='search')
]
