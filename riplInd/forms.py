from django import forms
from .models import product, contact, callme, subscribe, servicing
from django.forms import ModelForm,ModelChoiceField

class f_subscribe (ModelForm):
	class Meta:
		model = subscribe
		fields = ['email']
		widgets = {
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Your Email Address'}),
			}
class f_callme (ModelForm):
	class Meta:
		model = callme
		fields = ['number']
		widgets = {
			'number': forms.NumberInput(
			attrs={'placeholder': 'Request a Callback'}),
			}
class f_email(forms.Form):
	sender = forms.EmailField(max_length=45, label="Sender",error_messages={'required':"From field cannot be blank"})
	name = forms.CharField(max_length=45, label="Name",error_messages={'required':"Name cannot be blank",'max_length':"Use a smaller name"})	
	message = forms.CharField(max_length=1000, label="Message",error_messages={'required':"Message cannot be blank"})
	
class f_product(ModelForm):
	class Meta:
		model = product
		fields = ['title', 'desc', 'image']

class f_contact(ModelForm):
	reasons = [('General Inquiry','General Inquiry'),('Corporate Inquiry','Corporate Inquiry'),('Warranty & Services','Warranty & Services'),('Sales Inquiry','Sales Inquiry'),('Careers','Careers'),('Feedback & Suggestions','Feedback & Suggestions')]
	reason = forms.ChoiceField(choices=reasons, required=True)
	class Meta:
		model = contact
		fields = ['fname','lname','occupation','phone','reason','email','message']
		widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lname': forms.TextInput(
                attrs={'placeholder': 'Last Name'}),
            'occupation': forms.TextInput(
                attrs={'placeholder': 'Occupation'}),
            'phone': forms.NumberInput(
                attrs={'placeholder': 'Enter Your Phone Number'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Your Email Address'}),
			'message': forms.Textarea(
                attrs={'placeholder': 'Enter Your Message Here'}),
        }
class f_servicing(ModelForm):
	class Meta:
		model = servicing
		fields = ['fname','lname','serial','phone','country','email','message']
		widgets = {
            'fname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lname': forms.TextInput(
                attrs={'placeholder': 'Last Name'}),
            'serial': forms.TextInput(
                attrs={'placeholder': 'Invoice/Serial No.'}),
            'phone': forms.NumberInput(
                attrs={'placeholder': 'Enter Your Phone Number'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Your Email Address'}),
			'message': forms.Textarea(
                attrs={'placeholder': 'Enter Your Message Here'}),
        }