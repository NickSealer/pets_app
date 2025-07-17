from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
  class Meta:
    model = Pet
    fields = ['name', 'specie', 'age', 'age_unit', 'primary_color', 'secondary_color']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'specie': forms.Select(attrs={'class': 'form-control'}),
      'age': forms.TextInput(attrs={'class': 'form-control'}),
      'age_unit': forms.Select(attrs={'class': 'form-control'}),
      'primary_color': forms.Select(attrs={'class': 'form-control'}),
      'secondary_color': forms.Select(attrs={'class': 'form-control'})
    }