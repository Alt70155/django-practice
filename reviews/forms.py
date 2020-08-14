from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):

  class Meta:
    model = Review
    # 全てのモデルをフォームに表示する
    # fields = '__all__'
    # 表示するフォームを制限する場合
    # fields = ('store_name', 'title')
    # 表示しないフォームを書く場合
    exclude = ('created_at',)