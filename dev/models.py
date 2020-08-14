from django.db import models
from django.conf import settings

# Create your models here.

class Request(models.Model):
    BOOL = (
        (True, '○'),
        (False, '×')
    )
    # たぶんユーザーと日付は複合主キーにしてユニークにすべき
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='ユーザー名')
    date = models.DateField('日付')
    is_possible = models.BooleanField('出勤可能', choices=BOOL)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)