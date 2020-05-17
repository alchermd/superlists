from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Item

def home_page(request):
	if request.method == 'POST':
		item = Item.objects.create(text=request.POST['body'])
		return redirect('/lists/the-only-list/')

	return render(request, 'lists/home.html')

def view_list(request):
	return render(request, 'lists/list.html', {'items': Item.objects.all()})