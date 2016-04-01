from django.shortcuts import render
from article.models import Article
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

def home(request):
	blog = Article.objects.all()
	return render(request, 'home.html',{'blog_list':blog})

def detail(request,id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'post.html',{'post':post})
