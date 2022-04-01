from .models import Navbar

def navbar_processor(request):
	navbar_items = Navbar.objects.all()
	return {'navbar_items': navbar_items}