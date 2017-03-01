from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import unirest
import json
from django.http import JsonResponse
from .models import User, UserManager, Profile

def index(request):
    user_id = request.session.get('active_user_id')
    if Profile.objects.filter(user__id = user_id).exists():

        user = Profile.objects.get(user__id=user_id)
        other_users = Profile.objects.all().exclude(user__id=user_id)

        uSt = user.street_number
        uRoute = user.route
        uCity = user.city
        uState = user.state

        for other_user in other_users:
            oSt = other_user.street_number
            oRoute = other_user.route
            oCity = other_user.city
            oState = other_user.state

            url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+ uSt + ','+ uRoute + ',' + uCity + ',' + uState +'&destinations='+ oSt + ','+ oRoute + ',' + oCity + ',' + oState +'&key=AIzaSyBj4eaE79fE1cqdaq1XZALhzxCpKPd2F2I'
            headers={"X-Mashape-Key": "ABCDEFG12345"}

            response = unirest.get(url, headers=headers)
            data = response.body
            dist = data['rows'][0]['elements'][0]['distance']['value']
            dist = int(dist*0.000621371)

            other_user.distAway = dist

        data = {
            "user" : User.objects.get(id=user_id),
            "profile" : user,
            "other_users" : other_users,
            'flag' : True
            }

    else:
        data = {
            "user" : User.objects.get(id=user_id),
            'flag' : False
            }

    return render(request, 'main/index.html', data)
