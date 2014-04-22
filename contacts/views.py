'''
Created on Apr 9, 2014

@author: rchibana
'''

from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from contacts.models import Contact
import forms


class ContactView(DetailView):

    model = Contact
    template_name = "contact/contact.html"


class CreateContactView(CreateView):

    model = Contact
    template_name = 'contact/edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contact.list')


class ListContactView(ListView):

    model = Contact
    template_name = 'contact/contact_list.html'


class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'contact/edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contact.list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contact.edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'contact/delete_contact.html'

    def get_success_url(self):
        return reverse('contact.list')
