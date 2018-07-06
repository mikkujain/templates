from django.urls import include, path
#from django.conf.urls import url
from . import views
app_names = 'blog'

urlpatterns = [
	path('', views.post_list, name='post_list')
]