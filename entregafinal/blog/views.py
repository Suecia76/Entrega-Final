from django.shortcuts import render

def index(request):
    """
    Render the index page of the blog.
    """
    return render(request, 'blog/index.html')