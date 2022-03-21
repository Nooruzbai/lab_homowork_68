from django.http import JsonResponse
from django.views import View

from webapp.models import Article, User, Comment


class ArticleLikeUnlike(View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=self.kwargs.get('pk'))
        user = User.objects.get(pk=self.request.user.id)
        if user not in article.users.all():
            article.users.add(user)
            article.save()
            return JsonResponse({"like_quantity": article.users.count()})
        else:
            article.users.remove(user)
            article.save()
            return JsonResponse({"like_quantity": article.users.count()})


class CommentLikeUnlike(View):

    def get(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=self.kwargs.get('pk'))
        user = User.objects.get(pk=self.request.user.id)
        if user not in comment.users.all():
            comment.users.add(user)
            comment.save()
            return JsonResponse({"like_quantity": comment.users.count()})
        else:
            comment.users.remove(user)
            comment.save()
            return JsonResponse({"like_quantity": comment.users.count()})







