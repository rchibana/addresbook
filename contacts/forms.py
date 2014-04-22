'''
Created on Apr 11, 2014

@author: rchibana
'''
from django import forms

from contacts.models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    confim_email = forms.EmailField(
        label="Confirm email",
        required=True,
    )

    class Meta:
        model = Contact

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email']

        return  super(ContactForm, self).__init__(*args, **kwargs)

    def clean(self):

        if(self.cleaned_data.get('email') !=
           self.cleaned_data.get('confirm_email')):

            raise ValidationError(
                "Email addresses must match"
            )

        return self.cleaned_data
