from django.urls import path

from . import views

app_name = 'lists'

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('lists/new/', views.new_list, name='new_list'),
	path('lists/<pk>/add_item/', views.add_item, name='add_item'),
	path('lists/<pk>/', views.view_list, name='view_list'),
]