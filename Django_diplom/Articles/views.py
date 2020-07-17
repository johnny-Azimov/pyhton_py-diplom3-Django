from django.shortcuts import render

from Articles.models import Article


def article_show(request, slug):
    template = 'Articles/article.html'

    article = Article.objects.all().get(slug=slug)
    context = {
        'article': article
    }
    return render(request, template, context)
