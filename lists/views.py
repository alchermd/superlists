from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Item

def home_page(request):
	if request.method == 'POST':
		item = Item.objects.create(text=request.POST['body'])
		return redirect('/')

	return render(request, 'lists/home.html', {'items': Item.objects.all()})