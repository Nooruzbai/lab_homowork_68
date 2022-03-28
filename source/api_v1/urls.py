from django.urls import path, include

from .views import ArticleDetailView, ArticleSingleObjectView

app_name = 'api_v1'

urlpatterns = [
    path('get/articles/', ArticleDetailView.as_view(), name='article_detail_view' ),
    path('article/<int:pk>/', ArticleSingleObjectView.as_view(), name='article_single_object_view')
]


