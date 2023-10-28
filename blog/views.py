from django.shortcuts import render

posts =[
    {
        'author' : 'Silverter Stalone',
        'title' : 'Post 1',
        'content' : 'No coment :)',
        'date_posted' : 'March 19 , 2023',
    },
    {
        'author' : 'Silverter Stalone',
        'title' : 'Post 2',
        'content' : 'No coment :)',
        'date_posted' : 'March 19 , 2023',
    }   
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html' , context)

def about(request):
    return render(request, 'blog/about.html' , {'title' : 'About'})
    


