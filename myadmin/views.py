from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

User = get_user_model()

from users.forms import UserForm

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