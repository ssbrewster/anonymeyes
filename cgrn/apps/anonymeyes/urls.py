from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', view=views.IndexView.as_view(), name='index'),
                       url(r'^contact/$', view=views.ContactView.as_view(), name='contact'),
                       url(r'^thanks/$', view=views.ThanksView.as_view(), name='thanks'),
                       url(r'^about/$', view=views.AboutView.as_view(), name='about'),
                       url(r'^list/$', view=views.PatientListView.as_view(), name='list'),
                       url(r'^detail/(?P<pk>\d+)/$', view=views.PatientDetailView.as_view(), name='detail'),
                       url(r'^delete/(?P<pk>\d+)/$', view=views.PatientDeleteView.as_view(), name='delete'),
                       url(r'^create/$', view=views.PatientCreateView.as_view(), name='create'),
                       url(r'^update/(?P<pk>\d+)/$', view=views.PatientUpdateView.as_view(), name='update'),
                       url(r'^wizard/(?P<step>.+)/$', 'wizard', name='wizard_step'),
                       url(r'^wizard/$', 'wizard', name='wizard'),
)
