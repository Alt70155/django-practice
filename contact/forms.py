from django import forms


class ContactForm(forms.Form):
    CATEGORIES = (
        ('1', 'お仕事の依頼'),
        ('2', 'サイト内容に関する問い合せ'),
    )

    name = forms.CharField(
        label = 'お名前', max_length = 50,
        required = False, help_text = '※任意'
    )

    email = forms.EmailField(
        label = 'メールアドレス', required = False, help_text = '※任意'
    )
    text = forms.CharField(label = '問い合わせ内容', widget = forms.Textarea)
    category = forms.ChoiceField(label = 'カテゴリ', choices = CATEGORIES)