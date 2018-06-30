# django forms

from django import forms
#also use user models
from django.contrib.auth.models import User
from account.models import Personal_details
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)

	# exmaple photo class : resolution pixel or info about model
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2',]:
			self.fields[fieldname].help_text = None

	class Meta:
		model = User
		fields = ('username', 'first_name' , 'last_name','email', 'password1', 'password2')

	def save(self,commit = True):
		user =  super(RegistrationForm, self).save(commit = False)
		user.first_name =  self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EditProfileForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
			super(EditProfileForm, self).__init__(*args, **kwargs)
			for fieldname in ['password']:
				self.fields[fieldname].help_text = None
	class Meta:
		model = User
		fields = {
			'email',
			'first_name',
			'last_name',
			'password'

		}

class PersonalDetails(forms.ModelForm):  
    class Meta:  
        model = Personal_details 
        fields = "__all__"  
		
