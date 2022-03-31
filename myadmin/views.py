from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

User = get_user_model()

from users.forms import UserForm
from users.models import Role
from store.models import Treat

from .forms import TreatForm

@login_required(login_url='login')
def dashboard(request):
	return render(request, 'myadmin/dashboard.html')


@login_required(login_url='login')
def userProfile(request, pk):
	user = User.objects.get(id=pk)
	form = UserForm(instance=user)

	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return redirect('profile', pk)

	context = {
		'form': form,
		'user': user,
	}

	return render(request, 'myadmin/profile.html', context)


@login_required(login_url='login')
def userList(request):
	users = User.objects.all()

	return render(request, 'myadmin/user_list.html', {'users': users})


@login_required(login_url='login')
def createUser(request):
	form = UserForm()

	if request.method == 'POST':
		data = request.POST
		print(data)
		image = request.FILES.get('avatar')

		password = User.objects.make_random_password()
		print(password)

		user = User.objects.create_user(
			username=data['username'],
			email=data['email'],
			password=password
		)

		user.avatar = image
		user.first_name = data['first_name']
		user.last_name = data['last_name']
		if data['role']:
			user.role = Role.objects.get(id=data['role'])
		user.phone_number = data['phone_number']

		user.save()

		template = render_to_string('myadmin/email_template.html', {
			'name': user.first_name,
			'username': user.username,
			'email': user.email,
			'password': password
		})

		# After a user is created, need to send an email to that user with their
		# password and later on a link to change it.
		email = EmailMessage(
			'Account Created',
			template,
			settings.EMAIL_HOST_USER,
			[user.email]
		)

		email.fail_silently=False
		email.send()

		return redirect('dashboard')

	return render(request, 'myadmin/user_form.html', {'form': form})

@login_required(login_url='login')
def updateUser(request, pk):
	user = User.objects.get(id=pk)
	form = UserForm(instance=user)

	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
		else:
			messages.error(request, form.errors)

	context = {
		'form': form,
		'edit_user': user,
	}

	return render(request, 'myadmin/user_form.html', context)


@login_required(login_url='login')
def deleteUser(request, pk):
	user = User.objects.get(id=pk)

	if request.method == 'POST':
		user.delete()
		return redirect('user-list')



# Treat control

@login_required(login_url='login')
def treats_list(request):
	treats = Treat.objects.all()
	context = {'treats': treats}

	return render(request, 'myadmin/treats.html', context)

@login_required(login_url='login')
def addNewTreat(request):
	form = TreatForm()

	if request.method == 'POST':
		form = TreatForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dashboard')
	
	return render(request, 'myadmin/treat_form.html', {'form': form})

@login_required(login_url='login')
def updateTreat(request, pk):
	treat = Treat.objects.get(id=pk)
	form = TreatForm(instance=treat)

	if request.method == 'POST':
		form = TreatForm(request.POST, instance=treat)
		if form.is_valid():
			form.save()
			return redirect('treat-list')

	return render(request, 'myadmin/treat_form.html', {'form': form})


@login_required(login_url='login')
def deleteTreat(request, pk):
	treat = Treat.objects.get(id=pk)

	if request.method == 'POST':
		treat.delete()
		return redirect('treat-list')