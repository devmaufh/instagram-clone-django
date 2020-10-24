# Django
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def list_posts(request):
    """ List existing posts. """
    posts = {}
    return render(request, 'posts/feed.html', {'posts': posts})
