from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'ADMIN_edit/(?P<user_id>\d+)$', views.ADMIN_edit, name = 'ADMIN_edit'),
    url(r'ADMIN_delete/(?P<user_id>\d+)$', views.ADMIN_delete, name = 'ADMIN_delete'),
    url(r'ADMIN_save/(?P<user_id>\d+)$', views.ADMIN_save, name='ADMIN_save'),
    url(r'ADMIN_makeadmin/(?P<user_id>\d+)$', views.ADMIN_makeadmin, name = 'ADMIN_makeadmin')

]
