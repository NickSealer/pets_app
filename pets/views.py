from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import PetForm
from .models import Pet


class CreatePetView(LoginRequiredMixin, CreateView):
  model = Pet
  form_class = PetForm
  template_name = 'pets/create.html'
  success_url = reverse_lazy('pets')
  
  def form_valid(self, form):
    form.instance.owner = self.request.user
    messages.success(self.request, 'Pet created succesful!')
    return super().form_valid(form)
  
  def form_invalid(self, form):
    messages.error(self.request, 'Invalid pet!')
    return super().form_invalid(form)
