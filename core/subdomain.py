from django.conf import settings
from django_hosts import patterns, host
from django.contrib import admin


host_patterns = patterns(
    '',
    #host(r'', settings.ROOT_URLCONF, name=''),
    host(r'', settings.ROOT_URLCONF, name=''),
    host(r'www', settings.ROOT_URLCONF, name='www'),

    #host(r'admin', admin.site.urls , name='admin'),
    #host(r'users', "ubold.users.urls" , name='users'),
    #host(r'accounts', "ubold.accounts.urls", name='accounts'),

    host(r'blog', 'applications.blog.urls_subdomain', name='blog'),
    host(r'doc', 'applications.doc.urls_subdomain', name='doc'),
    host(r'test', 'applications.doc.urls_subdomain', name='test'),
    host(r'arbre', 'applications.arbre.urls_subdomain', name='arbre'),

    #host(r'book', 'applications.book.urls_subdomain', name='book'),
    host(r'forum', 'applications.forum.urls_subdomain', name='forum'),
    host(r'sample', 'applications.sample.urls_subdomain', name='sample'),
    #host(r'shelf', 'applications.shelf.urls_subdomain', name='shelf'),
    host(r'support' , 'applications.support.urls_subdomain'     , name='support'),

)

