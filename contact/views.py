from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .models import Customer

def contact(request):
	if request.method == 'POST':

		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		template = render_to_string('contact/email_template.html', {
			'name': name,
			'email': email,
			'phone': phone,
			'message': message,
		})

		customer, created = Customer.objects.get_or_create(
			email=email,
			defaults={'name': name, 'phone': phone},
		)

		email = EmailMessage( 
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			[settings.EMAIL_HOST_USER]
		)

		email.fail_silently=False
		email.send()
		return redirect('success')
	
	return render(request, 'contact/contact.html')


def successPage(request):
	return render(request, 'contact/success.html')