from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)$', views.index, name='index'),
    url(r'^edit_profile/(?P<user_id>\d+)$', views.edit_profile, name='edit_profile'),
    url(r'^edit_profile/edit_times$', views.view_times, name="view_times"),
    url(r'^edit_profile/update_times$', views.update_times, name='update_times'),
    url(r'^edit_profile/resize_image$', views.view_resize, name='view_resize'),
    url(r'^edit_profile/resized$', views.resize, name='resize'),
    url(r'^edit_profile/add_image$', views.image, name='add_image'),
    url(r'^edit_profile/ADMIN/delete/(?P<del_id>\d+)$', views.delete, name='delete')
]
