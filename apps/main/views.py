from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User, UserManager

def index(request):
    user_id = request.session.get('active_user_id')

    data = {
        "user" : User.objects.get(id=user_id),
        }

    return render(request, 'main/index.html', data)
