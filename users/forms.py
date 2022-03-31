from django.forms import ModelForm, Select
from django.contrib.auth import get_user_model

from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()
from .models import Role

class UserForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	
	phone = PhoneNumberField()

	class Meta:
		model = User
		fields = ['avatar', 'username', 'first_name', 'last_name', 'email', 
					'groups', 'role', 'phone_number']

		# widgets = {
		# 	'role': Select(),
		# }

class RoleForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(RoleForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	
	class Meta:
		model = Role
		fields = '__all__'
