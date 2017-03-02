from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import unirest
import json
from django.http import JsonResponse
from .models import User, UserManager, Profile, Match
from math import radians, cos, sin, asin, sqrt
from haversine import haversine

def index(request):
    user_id = request.session.get('active_user_id')
    if Profile.objects.filter(user__id = user_id).exists():

        user = Profile.objects.get(user__id=user_id)
        other_users = Profile.objects.all().exclude(user__id=user_id)

        lat1 = user.latitude
        lon1 = user.longtitude

        for other_user in other_users:
            lat2 = other_user.latitude
            lon2 = other_user.longtitude

            dist = haversine((lat1, lon1), (lat2, lon2), miles=True)

            if not Match.objects.filter(this_user_id=user_id).filter(profile_id=other_user.id).exists():
                Match.objects.create(
                    this_user = User.objects.get(id=user_id),
                    profile = Profile.objects.get(id=other_user.id),
                    distance = dist
                )
            else:
                Match.objects.filter(this_user_id=user.id).update(
                    this_user = User.objects.get(id=user_id),
                    profile = Profile.objects.get(id=other_user.id),
                    distance = dist
                )

        setDistance = Profile.objects.only('distAway').get(user_id = request.session['active_user_id']).distAway
        data = {
            "user" : User.objects.get(id=user_id),
            "profile" : user,
            "other_users" : Match.objects.filter(this_user_id=user_id).filter(distance__gte=setDistance),
            'flag' : True
            }

    else:
        data = {
            "user" : User.objects.get(id=user_id),
            'flag' : False
            }

    return render(request, 'main/index.html', data)
