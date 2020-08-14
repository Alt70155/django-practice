from django.views import generic
from .models import Request
from .forms import RequestCreateForm
from django.shortcuts import render, redirect
# Django備え付けのUserモデルを扱う為のimport
from django.contrib.auth.models import User

# Create your views here.

class Top(generic.TemplateView):
    template_name = 'dev/top.html'

class RequestList(generic.ListView):
    model = Request
    ordering = 'created_at'

class RequestCreate(generic.CreateView):
    model = Request
    form_class = RequestCreateForm

    def form_valid(self, form):
        req = form.save(commit=False)
        # ログイン機能を追加したらログインしているユーザーを設定する
        req.user = User.objects.get(id=1)
        req.save()
        return redirect('dev:top')