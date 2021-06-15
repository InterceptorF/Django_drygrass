
from django.shortcuts import render
from django.http import  HttpResponse

posts = [
    {
	'author': 'Chuck Forry',
	'title': 'Blog Post',
	'content': 'Second Post Content',
	'date_posted': 'June 14 2021'
  },
    {
        'author': 'Chuck Forry',
        'title': 'Blog Post',
        'content': 'Third Post Content',
        'date_posted': 'June 12 2021'
  }
]



def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})




