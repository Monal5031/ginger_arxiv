import arxiv
from django.core.paginator import Paginator, EmptyPage

ALL_QUERY = 'all:psychiatry OR all:therapy OR all:data science OR all:machine learning'
AUTHOR_QUERY = 'au:{0}'


def fetch_all_articles(num_articles, start=0):
    all_data = arxiv.query(
        search_query=ALL_QUERY,
        max_results=num_articles,
        sort_by='lastUpdatedDate',
        start=start
    )
    cleaned_data = list()
    for data in all_data:
        cleaned_data.append({
            'title': data['title'],
            'authors': data['authors'],
            'summary': data['summary'],
            'published': data['published']
        })
    return cleaned_data


def fetch_articles_by_author(author_name, num_articles, start=0):
    all_data = arxiv.query(
        search_query=AUTHOR_QUERY.format(author_name),
        max_results=num_articles,
        sort_by='lastUpdatedDate',
        start=start
    )
    cleaned_data = list()
    for data in all_data:
        cleaned_data.append({
            'title': data['title'],
            'published': data['published']
        })
    return cleaned_data


def paginate_view(request, query_set, page=None, num_items=None):
    """ Paginates view from queryset """
    if page is None:
        page = request.GET.get('page', default=1)
    if num_items is None:
        num_items = request.GET.get('num_items', default=10)
    paginator = Paginator(query_set, num_items)
    try:
        data_set = paginator.page(page)
    except EmptyPage:
        data_set = paginator.page(paginator.num_pages)
    return data_set, num_items, page
