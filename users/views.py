from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

User = get_user_model()

# Create your views here.
def home(request):
	return render(request, 'users/test_home.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST.get('email').lower()
		password = request.POST.get('password')

		try:
			user = User.objects.get(email=email)
		except:
			messages.error(request, 'User does not exist')
		
		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Username or password does not exist')

	return render(request, 'users/login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')