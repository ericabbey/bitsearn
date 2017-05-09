from django.conf.urls import url
from .import views
from geneology.views import geneo, treeview, expiring
from financial.views import stats, upgrade, wallet
app_name = "profile"
urlpatterns = [
    url(r'^$', views.profile_index, name='index'),
    url(r'^external/(?P<name>\w+)/$', views.ext_profile, name='ext'),
    url(r'^settings/$', views.profile_settings, name='settings'),
    url(r'^testimony/$', views.testiment, name='testiment'),
    url(r'^testimony/add$', views.new_test, name='add_test'),
    url(r'^news/$', views.news, name='news'),
    url(r'^support/$', views.support, name='support'),
    # geneo
    url(r'^geneology', geneo, name='geneo'),
    url(r'^tree-view/$', treeview, name='tree'),
    url(r'^expiring/$', expiring, name='expire'),
    # financial
    url(r'^wallet', wallet, name='wallet'),
    url(r'^upgrade/$', upgrade, name='upgrade'),
    url(r'^stats/$', stats, name='stats'),
]
