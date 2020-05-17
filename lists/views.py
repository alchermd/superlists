from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	ctx = {}
	if request.method == 'POST':
		ctx['new_item'] = request.POST['body']

	return render(request, 'lists/home.html', ctx)