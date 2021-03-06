from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Item, List

def home_page(request):
	return render(request, 'lists/home.html')

def view_list(request, pk):
	list_ = List.objects.get(pk=pk)
	return render(request, 'lists/list.html', {'list': list_})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['body'], list=list_)
	return redirect(f'/lists/{list_.id}/')

def add_item(request, pk):
	list_ = List.objects.get(pk=pk)
	Item.objects.create(text=request.POST['body'], list=list_)
	return redirect(f'/lists/{list_.id}/')