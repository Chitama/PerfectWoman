
from django.conf.urls import url

from . import views

app_name = 'portal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^form/$', views.form, name='form'),
]