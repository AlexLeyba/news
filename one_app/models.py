from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PodСategory(models.Model):
    name = models.CharField("Категория", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return "{} - {}".format(self.category, self.name)

    class Meta:
        verbose_name = 'Под категрия'
        verbose_name_plural = 'Под категории'


class News(models.Model):
    """Статья"""
    title = models.CharField("Заголовок", max_length=300)
    text = models.TextField("Тело")
    date = models.DateTimeField("дата", auto_now_add=True)
    picture = models.ImageField("Картинка", upload_to="images/", blank=True)
    chek = models.IntegerField("счетчик", default=0)
    category = models.ForeignKey(PodСategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    """Коментарии к статье"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Текст", max_length=1000)
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    chek = models.IntegerField("Лайки", default=0)
    like_chek = models.ManyToManyField(User, related_name="like_user")

    def __str__(self):
        return "{}".format(self.new)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
