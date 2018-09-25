# Generated by Django 2.1.1 on 2018-09-21 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('one_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('chek', models.IntegerField(default=0, verbose_name='Лайки')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='comment',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one_app.News'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]