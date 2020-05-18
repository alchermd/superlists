from django.urls import path

from . import views

app_name = 'lists'

urlpatterns = [
	path('new/', views.new_list, name='new_list'),
	path('<pk>/add_item/', views.add_item, name='add_item'),
	path('<pk>/', views.view_list, name='view_list'),
]