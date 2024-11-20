from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView
from exhibitions.models import Exhibition, Contact


class HomePage(ListView):
    model = Exhibition
    template_name = 'index.html'

class AboutUsPage(ListView):
    model = Exhibition
    template_name = 'about.html'
    
class GalleryPage(ListView):
    model = Exhibition
    template_name = 'gallery.html'

class ContactPage(CreateView):
    model = Contact
    fields = ('full_name', 'email', 'theme', 'description')
    template_name = 'contact.html'
    success_url = reverse_lazy('contact_page')

    def form_valid(self, form):
        messages.success(self.request, "Xabaringiz muvaffaqiyatli yuborildi!")
        return super().form_valid(form)