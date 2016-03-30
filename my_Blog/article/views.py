from django.shortcuts import render
from article.models import Article
from django.http import HttpResponse

# Create your views here.

def home(request):
	blog = Article.objects.all()
	return render(request, 'home.html',{'blog_list':blog})