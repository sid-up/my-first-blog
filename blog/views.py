from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    '''we create a variable for our QuerySet: posts. Treat this as the name of our QuerySet. From now on we can refer to it by this name.'''
    return render(request, 'blog/post_list.html', {'posts': posts})
