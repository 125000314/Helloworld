from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from mysite import views  

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATIC_ROOT }),
    (r'^hello/', views.hello),
    (r'^hello2/', views.hello2),
    (r'^hello3/', views.hello3),
    (r'^testJQuery/', views.testJQuery),
    (r'^hello5/', views.hello5),
    (r'^userInfo/', views.userInfo),
    (r'^userInfo2/', views.userInfo2),
    (r'^moni/', views.moni),
    (r'^login/', views.login),
    (r'^homePage/', views.homePage),
    (r'^admin/', include(admin.site.urls)),
)
