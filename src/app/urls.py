from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
	path('', views.index, name='index'),
	path('chain_analysis', views.chain_analysis, name='chain_analysis'),
]