from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views
from viewflow import views as viewflow
from helloworld.flows import HelloWorldFlow

urlpatterns = patterns(
    "",
    url(r'^helloworld/',
        include([
            HelloWorldFlow.instance.urls,
            url('^$', viewflow.ProcessListView.as_view(), name='index'),
            url('^tasks/$', viewflow.TaskListView.as_view(), name='tasks'),
            url('^queue/$', viewflow.QueueListView.as_view(), name='queue'),
            url(r'^details/(?P<process_pk>\d+)/$',
                viewflow.ProcessDetailView.as_view(), name='details')],
                namespace=HelloWorldFlow.instance.namespace),
            {'flow_cls': HelloWorldFlow}),
    #url(r'^flows/', include(viewflow.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
)