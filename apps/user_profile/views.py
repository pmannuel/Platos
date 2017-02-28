from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, UserManager, Profile
from ..schedules.models import Schedule, Day

def index(request, user_id):
    user_id = request.session.get('active_user_id')

    data = {
        "user" : User.objects.get(id=user_id),
        }

    return render(request, 'user_profile/index.html', data)

def view_times(request):
    active_user = User.objects.get(id = request.session['active_user_id'])
    context = {
    'schedule': Schedule.objects.get(user = request.session['active_user_id'])
    }
    return render(request, 'user_profile/edit_times.html', context)

def update_times(request):
    print "TEST"
    if request.method == 'POST':
        if 'Mon0to1' in request.POST:
            print "TRUE"
        else:
            print "FALSE"

        print request.POST['Mon2to3']
        mon = Day.objects.create(
            h0to1 = request.POST['Mon0to1'],
            h1to2 = request.POST['Mon0to1'],
            h2to3 = request.POST['Mon2to3'],
            h3to4 = request.POST['Mon3to4'],
            h4to5 = request.POST['Mon4to5'],
            h5to6 = request.POST['Mon5to6'],
            h6to7 = request.POST['Mon6to7'],
            h7to8 = request.POST['Mon7to8'],
            h8to9 = request.POST['Mon8to9'],
            h9to10 = request.POST['Mon9to10'],
            h10to11 = request.POST['Mon10to11'],
            h11to12 = request.POST['Mon11to12'],
            h12to13 = request.POST['Mon12to13'],
            h13to14 = request.POST['Mon13to14'],
            h14to15 = request.POST['Mon14to15'],
            h15to16 = request.POST['Mon15to16'],
            h16to17 = request.POST['Mon16to17'],
            h17to18 = request.POST['Mon17to18'],
            h18to19 = request.POST['Mon18to19'],
            h19to20 = request.POST['Mon19to20'],
            h20to21 = request.POST['Mon20to21'],
            h21to22 = request.POST['Mon21to22'],
            h22to23 = request.POST['Mon22to23'],
            h23to0 = request.POST['Mon23to0']
        )
        tue = Day.objects.create(
            h0to1 = request.POST['Tue0to1'],
            h1to2 = request.POST['Tue0to1'],
            h2to3 = request.POST['Tue2to3'],
            h3to4 = request.POST['Tue3to4'],
            h4to5 = request.POST['Tue4to5'],
            h5to6 = request.POST['Tue5to6'],
            h6to7 = request.POST['Tue6to7'],
            h7to8 = request.POST['Tue7to8'],
            h8to9 = request.POST['Tue8to9'],
            h9to10 = request.POST['Tue9to10'],
            h10to11 = request.POST['Tue10to11'],
            h11to12 = request.POST['Tue11to12'],
            h12to13 = request.POST['Tue12to13'],
            h13to14 = request.POST['Tue13to14'],
            h14to15 = request.POST['Tue14to15'],
            h15to16 = request.POST['Tue15to16'],
            h16to17 = request.POST['Tue16to17'],
            h17to18 = request.POST['Tue17to18'],
            h18to19 = request.POST['Tue18to19'],
            h19to20 = request.POST['Tue19to20'],
            h20to21 = request.POST['Tue20to21'],
            h21to22 = request.POST['Tue21to22'],
            h22to23 = request.POST['Tue22to23'],
            h23to0 = request.POST['Tue23to0']
        )
        wed = Day.objects.create(
            h0to1 = request.POST['Wed0to1'],
            h1to2 = request.POST['Wed0to1'],
            h2to3 = request.POST['Wed2to3'],
            h3to4 = request.POST['Wed3to4'],
            h4to5 = request.POST['Wed4to5'],
            h5to6 = request.POST['Wed5to6'],
            h6to7 = request.POST['Wed6to7'],
            h7to8 = request.POST['Wed7to8'],
            h8to9 = request.POST['Wed8to9'],
            h9to10 = request.POST['Wed9to10'],
            h10to11 = request.POST['Wed10to11'],
            h11to12 = request.POST['Wed11to12'],
            h12to13 = request.POST['Wed12to13'],
            h13to14 = request.POST['Wed13to14'],
            h14to15 = request.POST['Wed14to15'],
            h15to16 = request.POST['Wed15to16'],
            h16to17 = request.POST['Wed16to17'],
            h17to18 = request.POST['Wed17to18'],
            h18to19 = request.POST['Wed18to19'],
            h19to20 = request.POST['Wed19to20'],
            h20to21 = request.POST['Wed20to21'],
            h21to22 = request.POST['Wed21to22'],
            h22to23 = request.POST['Wed22to23'],
            h23to0 = request.POST['Wed23to0']
        )
        thu = Day.objects.create(
            h0to1 = request.POST['Thu0to1'],
            h1to2 = request.POST['Thu0to1'],
            h2to3 = request.POST['Thu2to3'],
            h3to4 = request.POST['Thu3to4'],
            h4to5 = request.POST['Thu4to5'],
            h5to6 = request.POST['Thu5to6'],
            h6to7 = request.POST['Thu6to7'],
            h7to8 = request.POST['Thu7to8'],
            h8to9 = request.POST['Thu8to9'],
            h9to10 = request.POST['Thu9to10'],
            h10to11 = request.POST['Thu10to11'],
            h11to12 = request.POST['Thu11to12'],
            h12to13 = request.POST['Thu12to13'],
            h13to14 = request.POST['Thu13to14'],
            h14to15 = request.POST['Thu14to15'],
            h15to16 = request.POST['Thu15to16'],
            h16to17 = request.POST['Thu16to17'],
            h17to18 = request.POST['Thu17to18'],
            h18to19 = request.POST['Thu18to19'],
            h19to20 = request.POST['Thu19to20'],
            h20to21 = request.POST['Thu20to21'],
            h21to22 = request.POST['Thu21to22'],
            h22to23 = request.POST['Thu22to23'],
            h23to0 = request.POST['Thu23to0']
        )
        fri = Day.objects.create(
            h0to1 = request.POST['Fri0to1'],
            h1to2 = request.POST['Fri0to1'],
            h2to3 = request.POST['Fri2to3'],
            h3to4 = request.POST['Fri3to4'],
            h4to5 = request.POST['Fri4to5'],
            h5to6 = request.POST['Fri5to6'],
            h6to7 = request.POST['Fri6to7'],
            h7to8 = request.POST['Fri7to8'],
            h8to9 = request.POST['Fri8to9'],
            h9to10 = request.POST['Fri9to10'],
            h10to11 = request.POST['Fri10to11'],
            h11to12 = request.POST['Fri11to12'],
            h12to13 = request.POST['Fri12to13'],
            h13to14 = request.POST['Fri13to14'],
            h14to15 = request.POST['Fri14to15'],
            h15to16 = request.POST['Fri15to16'],
            h16to17 = request.POST['Fri16to17'],
            h17to18 = request.POST['Fri17to18'],
            h18to19 = request.POST['Fri18to19'],
            h19to20 = request.POST['Fri19to20'],
            h20to21 = request.POST['Fri20to21'],
            h21to22 = request.POST['Fri21to22'],
            h22to23 = request.POST['Fri22to23'],
            h23to0 = request.POST['Fri23to0']
        )
        sat = Day.objects.create(
            h0to1 = request.POST['Sat0to1'],
            h1to2 = request.POST['Sat0to1'],
            h2to3 = request.POST['Sat2to3'],
            h3to4 = request.POST['Sat3to4'],
            h4to5 = request.POST['Sat4to5'],
            h5to6 = request.POST['Sat5to6'],
            h6to7 = request.POST['Sat6to7'],
            h7to8 = request.POST['Sat7to8'],
            h8to9 = request.POST['Sat8to9'],
            h9to10 = request.POST['Sat9to10'],
            h10to11 = request.POST['Sat10to11'],
            h11to12 = request.POST['Sat11to12'],
            h12to13 = request.POST['Sat12to13'],
            h13to14 = request.POST['Sat13to14'],
            h14to15 = request.POST['Sat14to15'],
            h15to16 = request.POST['Sat15to16'],
            h16to17 = request.POST['Sat16to17'],
            h17to18 = request.POST['Sat17to18'],
            h18to19 = request.POST['Sat18to19'],
            h19to20 = request.POST['Sat19to20'],
            h20to21 = request.POST['Sat20to21'],
            h21to22 = request.POST['Sat21to22'],
            h22to23 = request.POST['Sat22to23'],
            h23to0 = request.POST['Sat23to0']
        )
        sun = Day.objects.create(
            h0to1 = request.POST['Sun0to1'],
            h1to2 = request.POST['Sun0to1'],
            h2to3 = request.POST['Sun2to3'],
            h3to4 = request.POST['Sun3to4'],
            h4to5 = request.POST['Sun4to5'],
            h5to6 = request.POST['Sun5to6'],
            h6to7 = request.POST['Sun6to7'],
            h7to8 = request.POST['Sun7to8'],
            h8to9 = request.POST['Sun8to9'],
            h9to10 = request.POST['Sun9to10'],
            h10to11 = request.POST['Sun10to11'],
            h11to12 = request.POST['Sun11to12'],
            h12to13 = request.POST['Sun12to13'],
            h13to14 = request.POST['Sun13to14'],
            h14to15 = request.POST['Sun14to15'],
            h15to16 = request.POST['Sun15to16'],
            h16to17 = request.POST['Sun16to17'],
            h17to18 = request.POST['Sun17to18'],
            h18to19 = request.POST['Sun18to19'],
            h19to20 = request.POST['Sun19to20'],
            h20to21 = request.POST['Sun20to21'],
            h21to22 = request.POST['Sun21to22'],
            h22to23 = request.POST['Sun22to23'],
            h23to0 = request.POST['Sun23to0']
        )
        active_user = User.objects.get(id = request.session['active_user_id'])
        Schedule.objects.get(user = active_user).update(mon = mon, tue = tue, wed = wed, thu = thu, fri = fri, sat = sat, sun = sun)

    return redirect(reverse('user_profile:index'))

def edit_profile(request, user_id):
    user_id = request.session.get('active_user_id')

    data = {
        "user" : User.objects.get(id=user_id),
        }

    if request.method == "POST":
        user_id = request.session.get('active_user_id')

        Profile.objects.create(
            user = User.objects.get(id=user_id),
            birthday = request.POST['birthday'],
            occupation = request.POST['occupation'],
            company = request.POST['company'],
            street_number = request.POST['street_number'],
            route = request.POST['route'],
            city = request.POST['city'],
            state = request.POST['state'],
            postal_code = request.POST['postal_code'],
            about_me = request.POST['about_me']
        )

        return redirect(reverse('user_profile:index', kwargs={'user_id': user_id}))

    return render(request, 'user_profile/edit_profile.html', data)
