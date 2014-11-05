from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^contact/$', views.ContactView.as_view(), name='contact'),
                       url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),
                       url(r'^about/$', views.AboutView.as_view(), name='about'),
                       url(r'^list/$', views.PatientListView.as_view(), name='list'),
                       url(r'^detail/(?P<pk>\d+)/$', views.PatientDetailView.as_view(), name='detail'),
                       url(r'^delete/(?P<pk>\d+)/$', views.PatientDeleteView.as_view(), name='delete'),
                       url(r'^create/$', views.PatientCreateView.as_view(), name='create'),
                       url(r'^update/(?P<pk>\d+)/$', views.PatientUpdateView.as_view(), name='update'),
                       url(r'^wizard/(?P<step>.+)/$', 'wizard', name='wizard_step'),
                       url(r'^wizard/$', 'wizard', name='wizard'),
)
