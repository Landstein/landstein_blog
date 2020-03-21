from django.urls import include, path, re_path
from website import views

app_name = 'website'

urlpatterns = [
    re_path(r'^$', views.home_view, name='home'),

    re_path(r'^blog/$', views.blog_view, name='blog'),

    re_path(r'^works/$', views.works_view, name='works'),

    re_path(r'^(?P<permalink>.+)/$', views.page_view, name='page')
]
