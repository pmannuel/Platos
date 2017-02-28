from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import User, UserManager, Profile

def index(request, user_id):
    user_id = request.session.get('active_user_id')

    data = {
        "user" : User.objects.get(id=user_id),
        }

    return render(request, 'user_profile/index.html', data)

def edit_profile(request, user_id):
    user_id = request.session.get('active_user_id')
    active_user = User.objects.get(id=user_id),

    data = {
        "user" : User.objects.get(id=user_id),
        }

    return render(request, 'user_profile/edit_profile.html', data)
