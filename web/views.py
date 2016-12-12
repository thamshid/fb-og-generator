from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.forms.models import model_to_dict


# Create your views here.

def login(request, link):
	if not link:
		return render(request, 'index.html', {})
	url = UrlShort.objects.get(short=link)
	return render(request, 'redirect_page.html', {'obj':model_to_dict(url)})
	return HttpResponse(link)