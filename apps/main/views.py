from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User, UserManager, Profile

def index(request):
    user_id = request.session.get('active_user_id')
    if Profile.objects.filter(user__id = user_id).exists():
        data = {
            "user" : User.objects.get(id=user_id),
            "profile" : Profile.objects.get(user__id=user_id),
            "other_users" : Profile.objects.all().exclude(user__id=user_id),
            'flag' : True
            }
    else:
        data = {
            "user" : User.objects.get(id=user_id),
            'flag' : False
            }

    return render(request, 'main/index.html', data)
