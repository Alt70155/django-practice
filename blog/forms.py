from django import forms
from django.contrib.auth import get_user_model
from .models import Comment, Category, Tag

User = get_user_model()

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text'),
        widgets = {
            'text': forms.Textarea(attrs={'class': 'textarea'})
        }

class PostSearchForm(forms.Form):
    key_word = forms.CharField(
        label='キーワード', required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    category = forms.ModelChoiceField(
        label='カテゴリの選択', required=False,
        queryset=Category.objects.all(),
    )
    tags = forms.ModelMultipleChoiceField(
        label='タグの選択', required=False,
        queryset=Tag.objects.all(),
    )
    user = forms.ModelChoiceField(
        label='投稿者', required=False,
        queryset=User.objects.all(),
    )