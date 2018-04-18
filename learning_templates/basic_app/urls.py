from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name='basic_app'


urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login')

]
