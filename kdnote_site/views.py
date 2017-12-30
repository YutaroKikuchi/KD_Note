from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import Http404

from .models import CustomUser

# Create your views here.

#def login(request):
#	return render(request, 'kdnote_site/login.html',{})

def mypage(request):
	email = request.POST['email']
	passward = request.POST['password']
	user = authenticate(request,email=email,password=passward)
	if user is not None:
		login(request,user)
		return render(request, 'kdnote_site/mypage.html',{})
	else:
		raise Http404("user does not exist")
