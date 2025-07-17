from django.urls import path
from .views import CreatePetView, ListPetsView, DetailPetView, UpdatePetView, DeletePetView

urlpatterns = [
  path('pets/new/', CreatePetView.as_view(), name='create_pet'),
  path('pets/', ListPetsView.as_view(), name='pets'),
  path('pets/<int:pk>', DetailPetView.as_view(), name='pet'),
  path('pets/<int:pk>/edit', UpdatePetView.as_view(), name='edit_pet'),
  path('pets/<int:pk>/delete', DeletePetView.as_view(), name='delete_pet')
]