import json
from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from webapp.models import Article


class ArticleDetailView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = self.serializer_class(articles, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(
            serializer.validated_data,
            status=HTTPStatus.CREATED
        )

    def handle_exception(self, exc):
        if isinstance(exc, Exception):
            print(exc)
            return JsonResponse(data={'error': "Something went wrong"}, status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return super().handle_exception(exc)


class ArticleSingleObjectView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(article)

        return Response(serializer.data)

    def put(self, request, *args, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError as err:
            return Response(data=err.detail, status=HTTPStatus.BAD_REQUEST)

        return Response(
            data=serializer.validated_data,
        )

    def delete(self, request, *args, pk=None, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(article)
        article_ready = serializer.data['id']
        article.delete()
        return Response({'pk': article_ready})
