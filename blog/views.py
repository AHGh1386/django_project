from django.shortcuts import render
from .models import Post
# posts = [
#     {
#         'author': "Ali Darvishi",
#         'title': 'Post 1',
#         'content': 'Post 1 content (Some text)',
#         'date_posted': 'October 23, 2023'
#     },
#     {
#         'author': "Sahar Hashemi",
#         'title': 'Post 2',
#         'content': 'Post 2 content (Some text)',
#         'date_posted': 'October 20, 2023'
#     }

# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse("<h1>Blog Home</h1>")
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
