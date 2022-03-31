from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

User = get_user_model()

from users.forms import UserForm
from users.models import Role

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

		# Check if the other fields are present:
		# do something like for field in data:
		# 	if not username/email and exists then update the user

		return redirect('dashboard')

	return render(request, 'myadmin/user_form.html', {'form': form})

	# johny: FGc6SpUpdg
	# kim: FaaxqumXua
	# dp: qPM9HRFtfa
	# ac: t43P93SnzA

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