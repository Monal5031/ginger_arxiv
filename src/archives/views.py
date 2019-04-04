import dateutil.parser
from datetime import datetime, timedelta

from django.shortcuts import render

from src.archives.utils import fetch_articles_by_author, fetch_all_articles, paginate_view


def view_articles(request):
    articles = fetch_all_articles(100)
    articles, num_items, page = paginate_view(request, articles)

    before_30_days = datetime.today() - timedelta(days=30)

    final_articles = list()
    for i in articles:
        temp = dateutil.parser.parse(i['published'])
        i['published'] = temp.strftime('%m/%d/%Y')
        temp = temp.strptime(i['published'], '%m/%d/%Y')
        if temp >= before_30_days:
            final_articles.append(i)

    context = {
        'articles_list': final_articles,
        'num_items': num_items,
        'curr_page': page
    }

    return render(request, 'archives/all-articles.html', context)


def view_authors_articles(request):
    author_name = request.GET.get('author_name')
    authors_articles = fetch_articles_by_author(author_name, 100)
    authors_articles, num_items, page = paginate_view(request, authors_articles)

    before_30_days = datetime.today() - timedelta(days=30)

    final_articles = list()
    for i in authors_articles:
        temp = dateutil.parser.parse(i['published'])
        i['published'] = temp.strftime('%m/%d/%Y')
        temp = temp.strptime(i['published'], '%m/%d/%Y')
        if temp >= before_30_days:
            final_articles.append(i)

    context = {
        'author': author_name,
        'articles_list': final_articles,
        'num_items': num_items,
        'curr_page': page
    }

    return render(request, 'archives/articles_by_author.html', context)


def view_home(request):
    return render(request, 'archives/base.html')
