from django.urls import path
from .views import CreatePetView

urlpatterns = [
  path('pets/new/', CreatePetView.as_view(), name='create_pet'),
]