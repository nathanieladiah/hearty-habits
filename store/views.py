from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from contact.models import Customer
from .models import Order, Treat


def order(request, treat_id=None):

	treats = Treat.objects.all().order_by('name')

	# See if a treat id was passed in
	if treat_id:
		selected_treat = Treat.objects.get(id=treat_id)
	else:
		selected_treat = None

	if request.method == 'POST':

		name = request.POST.get('name')
		email = request.POST.get('email')

		customer, created = Customer.objects.get_or_create(
			email=email,
			defaults={'name': name},
		)

		treat_id = request.POST.get('treat')
		treat = Treat.objects.get(id=treat_id)

		count = request.POST.get('count')

		order = Order(treat=treat, count=count, customer=customer)
		order.save()

		template = render_to_string('store/confirm_email.html', {
			'order': order,
		})

		email_message = EmailMessage(
			'Order Confirmation',
			template,
			settings.EMAIL_HOST_USER,
			[email]
		)

		email_message.fail_silently=False
		email_message.content_subtype = 'html'
		email_message.send()

		return redirect('details', order.id)

	context = {
		'treats': treats,
		'selected_treat': selected_treat,
	}

	# TODO create a form for orders
	return render(request, 'store/order_form.html', context)


def orderDetails(request, pk):
	order = Order.objects.get(id=pk)
	context = {'order': order,}
	
	return render(request, 'store/order_details.html', context)


def confirmOrder(request, pk):
	order = Order.objects.get(uuid=pk)

	if request.method == 'POST':
		order.confirmed = True
		order.save()
		return redirect('order-success')

	context = {'order': order}
	return render(request, 'store/confirm_order.html', context)


def confirmSuccess(request):

	return render(request, 'store/success.html')