from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^login/', views.login_page, name='login'),
	url(r'^logout/', views.logout_account, name='logout'),
	url(r'^login_account/', views.login_account, name='login_account'),
	url(r'^new_user/', views.new_user, name='new_user'),
	url(r'^new_tidbit/', views.new_tidbit, name='new_tidbit'),
	url(r'^delete_account/', views.delete_account, name='delete_account'),
	url(r'^$', views.home, name='home'),
	url(r'^delete_tidbit/(?P<pk>.*)', views.delete_tidbit, name='delete'),
	url(r'^settings/', views.settings_page, name='settings'),
	url(r'^(?P<username>[\w\-]+)/$', views.profile, name='profile'),
]

urlpatterns += staticfiles_urlpatterns()