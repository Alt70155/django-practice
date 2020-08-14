from django.shortcuts import render
from .models import Diary

# Create your views here.
def top(request):
  context = {
    # .allでデータを取得し、diary_listという名前でテンプレートファイルへ渡す
    'diary_list': Diary.objects.all(),
  }
  return render(request, 'diaries/diary_list.html', context)
