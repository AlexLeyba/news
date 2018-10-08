# привести все с норм вид, сделать вход по соц сетям
from django.shortcuts import render, redirect
from django.views.generic import View
from one_app.models import News, Comment, Category
from one_app.forms import CommentForm, Search
from django.db.models import Q
from django.core.paginator import Paginator

class ListNews(View):
    """Список новостей"""

    def get(self, request):
        news = News.objects.all()
        paginator = Paginator(news, 2)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "one_app/list.html", {"news": contacts})


class OneNew(View):
    """вывод одной новости"""

    def get(self, request, pk):
        single = News.objects.get(id=pk)
        single.chek += 1
        single.save()
        last_news = News.objects.order_by('-id')[0:3]
        cat = News.objects.filter(category=single.category)[0:6]
        comment = Comment.objects.filter(new=pk)
        form = CommentForm()
        return render(request, "one_app/single.html", {"single": single, "form": form, "comment": comment,
                      "last_news": last_news})

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


class Category_View(View):
    """Вововд статей по категориям"""

    def get(self, request, category_slug):
        category = News.objects.filter(category__slug=category_slug)
        # category.save()
        return render(request, "one_app/category.html", {"category": category})


class Search_View(View):
    """Поиск по сайту"""

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get('q')
        founded = News.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return render(request, "one_app/search.html", {"founded": founded})



