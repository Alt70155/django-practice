# Generated by Django 3.0.5 on 2020-07-31 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリ')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='タグ')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='本文')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post', verbose_name='どの記事へのコメントか')),
            ],
        ),
    ]
