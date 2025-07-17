from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid:
      user = form.save()
      login(request, user)
      return redirect('dashboard')
  else:
    form = SignupForm()
  
  return render(request, 'auth/signup.html', {'form': form})

@login_required
def dashboard(request):
  return render(request, 'dashboard.html')