from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import CustomUser

# Create your views here.

def login(request):
	return render(request, 'kdnote_site/login.html',{})

def mypage(request):
	login_id = request.POST.get('login_id')
	userdata = get_object_or_404(CustomUser, pk=login_id)

	return render(request, 'kdnote_site/mypage.html',{})