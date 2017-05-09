from django.conf.urls import url
from .views import geneo, treeview, expiring

app_name = "geneology"
urlpatterns = [
    url(r'^$', geneo, name='index'),
    url(r'^tree-view/$', treeview, name='tree'),
    url(r'^expiring/$', expiring, name='expire'),
]
