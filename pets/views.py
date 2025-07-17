from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
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
  
class ListPetsView(LoginRequiredMixin, ListView):
  model = Pet
  template_name = 'pets/pets.html'
  context_object_name = 'pets'
  ordering = ['-name']
  paginate_by = 10
  
  def get_queryset(self):
    return Pet.objects.filter(owner=self.request.user)
  
class DetailPetView(LoginRequiredMixin, DetailView):
  model = Pet
  template_name = 'pets/pet.html'
  context_object_name = 'pet'
  
  def get_queryset(self):
    return Pet.objects.filter(owner=self.request.user)
  
  
