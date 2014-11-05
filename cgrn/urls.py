from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='anonymeyes')),
    url(r'^anonymeyes/', include('anonymeyes.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
)
