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
            param = 'mon_schedule__' + '_' + i + 'to' + '_' + i+1
            if Schedule.objects.filter(param).filter(user = session['user_id']) == True:
                mon.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'tue_schedule__' + '_' + i + 'to' + '_' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                tue.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'wed_schedule__' + '_' + i + 'to' + '_' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                wed.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'thu_schedule__' + '_' + i + 'to' + '_' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                thu.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'fri_schedule__' + '_' + i + 'to' + '_' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                fri.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'sat_schedule__' + '_' + i + 'to' + '_' + i+1
            if Schedule.objects.filter(param).filter(user = request.session['user_id']) == True:
                sat.append(Schedule.objects.filter(param).exclude(user = request.session['user_id']))
            i += 1
        i = 0
        while(i<=23):
            param = 'sun_schedule__' + '_' + i + 'to' + '_' + i+1
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
    _9to10 = models.BooleanField(False)
    _10to11 = models.BooleanField(False)
    _11to12 = models.BooleanField(False)
    _12to13 = models.BooleanField(False)
    _13to14 = models.BooleanField(False)
    _14to15 = models.BooleanField(False)
    _15to16 = models.BooleanField(False)
    _16to17 = models.BooleanField(False)
    _17to18 = models.BooleanField(False)
    _18to19 = models.BooleanField(False)
    _19to20 = models.BooleanField(False)
    _20to21 = models.BooleanField(False)
    _21to22 = models.BooleanField(False)
    _22to23 = models.BooleanField(False)
    _23to0 = models.BooleanField(False)
    _0to1 = models.BooleanField(False)
    _1to2 = models.BooleanField(False)
    _2to3 = models.BooleanField(False)
    _3to4 = models.BooleanField(False)
    _4to5 = models.BooleanField(False)
    _5to6 = models.BooleanField(False)
    _6to7 = models.BooleanField(False)
    _7to8 = models.BooleanField(False)
    _8to9 = models.BooleanField(False)

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
