from django.shortcuts import render

from src.archives.utils import fetch_articles_by_author, fetch_all_articles, paginate_view


def view_articles(request):
    articles = fetch_all_articles(100)
    articles, num_items, page = paginate_view(request, articles)

    context = {
        'articles_list': articles,
        'num_items': num_items,
        'curr_page': page
    }

    return render(request, 'archives/all-articles.html', context)


def view_authors_articles(request, author_name):
    authors_articles = fetch_articles_by_author(author_name, 100)
    authors_articles, num_items, page = paginate_view(request, authors_articles)

    context = {
        'author': author_name,
        'articles_list': authors_articles,
        'num_items': num_items,
        'curr_page': page
    }

    return render(request, '', context)


def view_home(request):
    return render(request, 'archives/base.html')
