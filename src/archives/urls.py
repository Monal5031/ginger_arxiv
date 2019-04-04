from django.conf.urls import url

from src.archives.views import view_articles, view_authors_articles

urlpatterns = [
    url('^articles/?$', view_articles, name='all-articles'),
    url('^authors/(?P<author_name>[-\w]+)$', view_authors_articles, name='articles-by-author')
]
