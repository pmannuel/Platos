from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import unirest
import json
from django.http import JsonResponse
from .models import User, UserManager, Profile, Match, Images, Schedule, Day
from math import radians, cos, sin, asin, sqrt
from haversine import haversine

def index(request):
    user_id = request.session.get('active_user_id')
    if Profile.objects.filter(user__id = user_id).exists():

        user = Profile.objects.get(user__id=user_id)
        other_users = Profile.objects.all().exclude(user_id=user_id)

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
                    distance = dist,
                    image = Images.objects.get(user_id=other_user.id),
                    schedule = Schedule.objects.get(user_id = other_user.id)
                )
            else:
                Match.objects.filter(this_user_id=user.id).filter(profile_id=other_user.id).update(
                    this_user = User.objects.get(id=user_id),
                    profile = Profile.objects.get(id=other_user.id),
                    distance = dist,
                    image = Images.objects.get(user_id=other_user.id),
                    schedule = Schedule.objects.get(user_id = other_user.id)
                )


        setDistance = Profile.objects.only('distAway').get(user_id = request.session['active_user_id']).distAway

        if not 'genderpick' in request.session:
            profile = Profile.objects.get(user = request.session.get('active_user_id'))
            if profile.gender == "male":
                genderpick = "female"
            if profile.gender == "female":
                genderpick = "male"
        else:
            genderpick = request.session['genderpick']
        if genderpick == "whatever":
            match = Match.objects.filter(this_user_id=user_id).filter(distance__gte=setDistance)
        else:
            match = Match.objects.filter(this_user_id=user_id).filter(distance__gte=setDistance).filter(profile__gender=genderpick)
        # if not 'interestday' in request.session:
        #     day = 'mon'
        # else:
        #     day = request.session['interestday']
        # if day == 'mon':
        #     exclude = ""
        #     i = 0
        #     while i < 23:
        #         check = 'mon__h' + str(i) + 'to' + str(i+1)
        #         if Schedule.objects.filter(user_id = request.session.get('active_user_id')).filter(**{ check: False }):
        #             exclude += ".exclude(" + check + ")"
        #         i += 1
        #     if Schedule.objects.filter(user_id = request.session.get('active_user_id')).filter(mon__h23to0 = False):
        #         exclude += ".exclude(" + check + ")"
        #     print exclude

        # will edit in the morning, am going to change to array values for ease of use
        data = {
            "user" : User.objects.get(id=user_id),
            "profile" : user,

            "other_users" : Match.objects.filter(this_user_id=user_id).filter(distance__lte=setDistance),

            'flag' : True,
            'img' : Images.objects.filter(user_id = user_id),
            'genderpick' : genderpick,
            # 'day' : day
            }

    else:
        data = {
            "user" : User.objects.get(id=user_id),
            'flag' : False,
            'img' : Images.objects.filter(user_id = user_id)
            }

    return render(request, 'main/index.html', data)

def changedistance(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user = request.session.get('active_user_id'))
        profile.distAway = request.POST['distance']
        profile.save()
        request.session['genderpick'] = request.POST['gender']
        request.session['interestday'] = request.POST['day']
    return redirect(reverse('main:index'))
