from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User, UserManager, Profile

def index(request):
    user_id = request.session.get('active_user_id')

    data = {
        "user" : User.objects.get(id=user_id),
        # "profile" : Profile.objects.get(user__id=user_id),
        # "other_users" : Profile.objects.all().exclude(user__id=user_id),
        }

    return render(request, 'main/index.html', data)
