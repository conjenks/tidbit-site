from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tidbit.models import Tidbit, Profile
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import NewAccountForm

def login_page(request):
	form = NewAccountForm()
	template = loader.get_template('tidbit/login.html/')
	context = {'form': form}
	return HttpResponse(template.render(context, request))

@login_required
def home(request):
	tidbits = Tidbit.objects.all()
	user = request.user
	template = loader.get_template('tidbit/home.html')
	context = {'tidbits': tidbits, 'user': user}
	return HttpResponse(template.render(context, request))

@login_required
def profile(request, username):
	user = User.objects.get(username=username)
	tidbits = Tidbit.objects.filter(user=user)
	template = loader.get_template('tidbit/profile.html')
	context = {'user': user, 'tidbits': tidbits}
	return HttpResponse(template.render(context, request))

@login_required
def settings_page(request):
	return HttpResponse(render(request, 'tidbit/settings.html/'))

@login_required
def new_tidbit(request):
	text = request.POST.__getitem__('new_tidbit')
	tidbit = Tidbit.objects.create(user=request.user, text=text)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def login_account(request):
	username = request.GET.__getitem__('username')
	password = request.GET.__getitem__('password')

	user = authenticate(username=username, password=password)
	login(request, user)
	return redirect('home')

def new_user(request):
	form = NewAccountForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		email = form.cleaned_data['email']

		try:
			user = User.objects.create_user(username, email, password)
		except:
			return HttpResponse("That username is already taken. Please try a different one.")

		user.first_name = first_name
		user.last_name = last_name
		user.save()

		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('home')

	else:
		return HttpResponse("The form you submitted was invalid. Please enter appropriate input.")

@login_required
def logout_account(request):
	logout(request)
	return redirect('login')

@login_required
def delete_tidbit(request, pk):
	tidbit = Tidbit.objects.get(pk=pk)
	tidbit.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_account(request):
	delete_bool = request.POST.__getitem__('delete')
	if delete_bool == "yes":
		request.user.delete()
		return redirect('login')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


