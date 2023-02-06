from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from users.forms import RegisterForm, EditForm, UserProfileForm
from users.models import UserProfile

from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context)
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido {username}'
                }
                return render(request, 'index.html', context)

        form = AuthenticationForm()
        context = {
            'form': form,
            'message': 'Usuario o contraseña incorrectos'
        }
        return render(request, 'users/login.html', context)


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm() 
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)

            return redirect('login')
        context = {
            'form': form,
            'message': form.errors
        }
        return render(request, 'users/register.html', context)


@login_required 
def edit_user(request,):
    user = request.user
    if request.method == 'GET':
        form = EditForm(initial = {
            'username': user.username,            
            'first_name': user.first_name,
            'last_name': user.last_name
        })
        context = {
            'form': form
        }
        return render(request, 'users/edit.html', context)
    elif request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('index')
        context = {
            'form': form,
            'message': form.errors
        }
        return render(request, 'users/edit.html', context)
    
@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)

def edit_user_profile(request):
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone': request.user.profile.phone,
            'birth_date': request.user.profile.birth_date,
            'profile_picture': request.user.profile.profile_picture
        }) 
        context = {
            'form': form
        }
        return render(request, 'users/update.html', context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.phone = form.cleaned_data.get('phone')
            request.user.profile.birth_date = form.cleaned_data.get('birth_date')
            request.user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            request.user.profile.save()            
            return redirect('index')
        context = {
            'form': form,
            'message': form.errors
        }
        return render(request, 'users/update.html', context)
    
    

    
    
            
            
    
    



            
        
                


         



            




       