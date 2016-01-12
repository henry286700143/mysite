from django.conf.urls import patterns,include,url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'mysite.views.first_page'),
	url(r'^west/', include('west.urls')),
)
