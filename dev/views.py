from django.views import generic
from .models import Request
from django.shortcuts import render

# Create your views here.

class RequestList(generic.ListView):
    model = Request
    ordering = '-created_at'