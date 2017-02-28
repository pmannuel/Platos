from __future__ import unicode_literals
from ..login_register.models import User
from django.db import models

# Create your models here.
class ScheduleManager(models.Manager):
    def isMatch(self, request):
        mon = []
        tue = []
        wed = []
        thu = []
        fri = []
        sat = []
        sun = []
        i = 0
        while(i<=23):
            param = 'mon_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = session['user_id']) == True:
                mon.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'tue_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                tue.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'wed_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                wed.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'thu_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                thu.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'fri_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                fri.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'sat_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                sat.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'sun_schedule__h' + i + 'to' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                sun.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        matches = {
        'mon': mon,
        'tue': tue,
        'wed': wed,
        'thu': thu,
        'fri': fri,
        'sat': sat,
        'sun':sun
        }
        return matches
class Day(models.Model):
    h9to10 = models.BooleanField(default=False)
    h10to11 = models.BooleanField(default=False)
    h11to12 = models.BooleanField(default=False)
    h12to13 = models.BooleanField(default=False)
    h13to14 = models.BooleanField(default=False)
    h14to15 = models.BooleanField(default=False)
    h15to16 = models.BooleanField(default=False)
    h16to17 = models.BooleanField(default=False)
    h17to18 = models.BooleanField(default=False)
    h18to19 = models.BooleanField(default=False)
    h19to20 = models.BooleanField(default=False)
    h20to21 = models.BooleanField(default=False)
    h21to22 = models.BooleanField(default=False)
    h22to23 = models.BooleanField(default=False)
    h23to0 = models.BooleanField(default=False)
    h0to1 = models.BooleanField(default=False)
    h1to2 = models.BooleanField(default=False)
    h2to3 = models.BooleanField(default=False)
    h3to4 = models.BooleanField(default=False)
    h4to5 = models.BooleanField(default=False)
    h5to6 = models.BooleanField(default=False)
    h6to7 = models.BooleanField(default=False)
    h7to8 = models.BooleanField(default=False)
    h8to9 = models.BooleanField(default=False)

class Schedule(models.Model):
    user = models.ForeignKey(User, related_name = 'schedule_user')
    mon = models.ForeignKey(Day, related_name = 'mon_schedule')
    tue = models.ForeignKey(Day, related_name = 'tue_schedule')
    wed = models.ForeignKey(Day, related_name = 'wed_schedule')
    thu = models.ForeignKey(Day, related_name = 'thu_schedule')
    fri = models.ForeignKey(Day, related_name = 'fri_schedule')
    sat = models.ForeignKey(Day, related_name = 'sat_schedule')
    sun = models.ForeignKey(Day, related_name = 'sun_schedule')
    objects = ScheduleManager()
