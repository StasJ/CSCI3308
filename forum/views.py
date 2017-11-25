from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

class IndexView(ListView):
    template_name = 'forum/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

