import arxiv

ALL_QUERY = 'all:psychiatry OR all:therapy OR all:data science OR all:machine learning'
AUTHOR_QUERY = 'au:{0}'


def fetch_all_articles(n):
    all_data = arxiv.query(
        search_query=ALL_QUERY,
        max_results=n,
        sort_by='lastUpdatedDate'
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


def fetch_articles_by_author(name, n):
    all_data = arxiv.query(
        search_query=AUTHOR_QUERY.format(name),
        max_results=n,
        sort_by='lastUpdatedDate'
    )
    cleaned_data = list()
    for data in all_data:
        cleaned_data.append({
            'title': data['title'],
            'published': data['published'],
            'author': name
        })
    return cleaned_data
