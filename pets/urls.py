from django.urls import path
from .views import CreatePetView, ListPetsView

urlpatterns = [
  path('pets/new/', CreatePetView.as_view(), name='create_pet'),
  path('pets/', ListPetsView.as_view(), name='pets')
]