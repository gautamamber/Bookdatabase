from django.conf.urls import url, include
from django.contrib import admin
from . import views
# from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
password_reset_complete)

urlpatterns = [
	url(r'^$',views.home, name= 'home'),
	url(r'^login/$',login,{'template_name' : 'account/login.html'}),
	url(r'^logout/$',logout, {'template_name' : 'account/logout.html'}),
	url(r'^register/$',views.register, name = 'register'),
	#read data 
	url(r'^profile/$', views.profile, name = 'profile'),
	#edit
	url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
	#change password
	
	url(r'^change_password/$', views.change_password, name= 'change_password'),
	url(r'^personal_details/$', views.personal_details_show, name= 'personal_details'),
	
	 url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    ]

handler404 = views.error_404
handler500 = views.error_500