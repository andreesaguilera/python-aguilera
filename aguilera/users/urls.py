from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import login_view, register_view, edit_user, profile_view, edit_user_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html')),
    path('signup/', register_view),   
    path('edit/', edit_user),
    path('profile/', profile_view),    
    path('update/', edit_user_profile),
]