from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy


class ContactView(FormView):
    template_name = 'Contact.html'
    form_class = ContactForm
    success_url= reverse_lazy('contact')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
