# подключить summernot вывод картинок новости. вывод категорий в меню сайта, поиск по названию статьи
from django.shortcuts import render, redirect
from django.views.generic import View
from one_app.models import News, Comment
from one_app.forms import CommentForm

class ListNews(View):
    """Список новостей"""
    def get(self, request):
        news = News.objects.all()
        return render(request, "one_app/list.html", {"news": news})


class OneNew(View):
    """вывод одной новости"""
    def get(self, request, pk):
        single = News.objects.get(id=pk)
        single.chek += 1
        single.save()
        comment = Comment.objects.filter(new=pk)
        form = CommentForm()
        return render(request, "one_app/single.html", {"single": single, "form": form, "comment": comment},)


    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = News.objects.get(id=pk)
            form.save()
            return redirect("/single/{}".format(pk))
        else:
            pass

class Like(View):
    """Лайки для комментариев"""
    def get(self, request, pk, post_pk):
        comment = Comment.objects.get(id=pk)
        if request.user in comment.like_chek.all():
            pass
        else:
            comment.chek += 1
            comment.like_chek.add(request.user.id)
            comment.save()
        return redirect("/single/{}".format(post_pk))


