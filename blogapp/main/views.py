from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from main import models

# Create your views here.

def index(request):

    latest_articles = models.Article.objects.all().order_by('-createdAt')[:10]

    context = {
        "latest_articles" : latest_articles
    }
    
    return render(request, 'main/index.html', context)


def article(request, pk):

    """ try:
        article = models.Article.objects.get(pk = pk)
    except:
        raise Http404() """

    article = get_object_or_404(models.Article, pk = pk)
    

    context = {
        "article" : article
    }

    return render(request, 'main/article.html', context)


def author(request, pk):
    author = get_object_or_404(models.Author, pk = pk)

    context = {
        "author": author
    }

    return render(request, 'main/author.html', context)


def create_article(request):

#Fetching data from DB and sending it to frontend
    authors = models.Author.objects.all()
    context = {
        "authors" : authors
    }

#Fetching data from form and updating it to DB
    if request.method == "POST":
        article_data = {
            "title" : request.POST['title'],
            "content" : request.POST['content'],
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.get(pk = request.POST['author'])
        article.authors.set([author])     #Since Author is a many to many field, it expects a list as argument
        context["success"] = True

 
    return render(request, 'main/create_article.html', context)