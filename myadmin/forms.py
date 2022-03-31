from django.forms import  ModelForm

from store.models import Treat

class TreatForm(ModelForm):
	class Meta:
		model = Treat
		fields = '__all__'