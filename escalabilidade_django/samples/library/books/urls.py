from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('books.views',
    url('^$', 'list_books'),
)
