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
            if Schedule.objects.filter(mon_schedule__(i)_(i+1)).filter(user = session['user_id']) == True:
                mon.append(Schedule.objects.filter(mon_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
            i += 1
        i = 0
        while(i<=23):
            if Schedule.objects.filter(tue_schedule__(i)_(i+1)).filter(user = request.session['user_id']) == True:
                tue.append(Schedule.objects.filter(tue_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
            i += 1
        i = 0
        while(i<=23):
            if Schedule.objects.filter(wed_schedule__(i)_(i+1)).filter(user = request.session['user_id']) == True:
                wed.append(Schedule.objects.filter(wed_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
            i += 1
        i = 0
        while(i<=23):
            if Schedule.objects.filter(thu_schedule__(i)_(i+1)).filter(user = request.session['user_id']) == True:
                thu.append(Schedule.objects.filter(thu_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
            i += 1
        i = 0
        while(i<=23):
            if Schedule.objects.filter(fri_schedule__(i)_(i+1)).filter(user = request.session['user_id']) == True:
                fri.append(Schedule.objects.filter(fri_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
            i += 1
        i = 0
        while(i<=23):
            if Schedule.objects.filter(sat_schedule__(i)_(i+1)).filter(user = request.session['user_id']) == True:
                sat.append(Schedule.objects.filter(sat_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
            i += 1
        i = 0
        while(i<=23):
            if Schedule.objects.filter(sun_schedule__(i)_(i+1)).filter(user = request.session['user_id']) == True:
                sun.append(Schedule.objects.filter(sun_schedule__(i)_(i+1).exclude(user = request.session['user_id'])))
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



class Day(models.Model):
    9_10 = models.BooleanField(False)
    10_11 = models.BooleanField(False)
    11_12 = models.BooleanField(False)
    12_13 = models.BooleanField(False)
    13_14 = models.BooleanField(False)
    14_15 = models.BooleanField(False)
    15_16 = models.BooleanField(False)
    16_17 = models.BooleanField(False)
    17_18 = models.BooleanField(False)
    18_19 = models.BooleanField(False)
    19_20 = models.BooleanField(False)
    20_21 = models.BooleanField(False)
    21_22 = models.BooleanField(False)
    22_23 = models.BooleanField(False)
    23_0 = models.BooleanField(False)
    0_1 = models.BooleanField(False)
    1_2 = models.BooleanField(False)
    2_3 = models.BooleanField(False)
    3_4 = models.BooleanField(False)
    4_5 = models.BooleanField(False)
    5_6 = models.BooleanField(False)
    6_7 = models.BooleanField(False)
    7_8 = models.BooleanField(False)
    8_9 = models.BooleanField(False)
