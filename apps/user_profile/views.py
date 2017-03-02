from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, UserManager, Profile, Images
import unirest
import json
from ..schedules.models import Schedule, Day
from .forms import ImgForm
from PIL import Image

def index(request, user_id):
    user_id = request.session.get('active_user_id')
    data = {
        "user" : User.objects.get(id=user_id),
        }
    return render(request, 'user_profile/index.html', data)

def view_resize(request):
    context = {
    'img': Images.objects.filter(user_id = request.session['active_user_id']),
    'user': User.objects.get(id = request.session['active_user_id'])
    }
    return render(request, 'user_profile/image_resize.html', context)

def resize(request):
    user = str(request.session.get('active_user_id'))
    right = float(request.POST['cropx'])
    down = float(request.POST['cropy'])
    image = Images.objects.only('avatar').get(user_id = request.session['active_user_id']).avatar
    print image
    im = Image.open(image)
    box = (right, down, 250+right, 250+down)
    if im.size[0] > 750:
        basewidth = 750
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    img2 = im.crop(box)
    savelocation = 'Platos/media/login_register/avatar/' + user + '.jpg'
    img2.save(savelocation,'JPEG')
    location = 'login_register/avatar/' + user + '.jpg'
    user_id = request.session.get('active_user_id')
    delete = Images.objects.filter(user = user_id).delete()
    update = Images.objects.filter(user = user_id).create(avatar = location, user_id = user_id, resize = True)
    return redirect(reverse('user_profile:edit_profile', kwargs={'user_id': request.session['active_user_id']}))

def image(request):
    user_id = request.session.get('active_user_id')
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            delete = Images.objects.filter(user = user_id).delete()
            update = Images.objects.filter(user = user_id).create(avatar=request.FILES['imgfile'], user_id = user_id, resize = False)
    return redirect(reverse('user_profile:view_resize'))

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
            bMon0to1 = True
        else:
            bMon0to1 = False

        if 'Mon1to2' in request.POST:
            bMon1to2 = True
        else:
            bMon1to2 = False

        if 'Mon2to3' in request.POST:
            bMon2to3 = True
        else:
            bMon2to3 = False

        if 'Mon3to4' in request.POST:
            bMon3to4 = True
        else:
            bMon3to4 = False

        if 'Mon4to5' in request.POST:
            bMon4to5 = True
        else:
            bMon4to5 = False

        if 'Mon5to6' in request.POST:
            bMon5to6 = True
        else:
            bMon5to6 = False

        if 'Mon6to7' in request.POST:
            bMon6to7 = True
        else:
            bMon6to7 = False

        if 'Mon7to8' in request.POST:
            bMon7to8 = True
        else:
            bMon7to8 = False

        if 'Mon8to9' in request.POST:
            bMon8to9 = True
        else:
            bMon8to9 = False

        if 'Mon9to10' in request.POST:
            bMon9to10 = True
        else:
            bMon9to10 = False

        if 'Mon10to11' in request.POST:
            bMon10to11 = True
        else:
            bMon10to11 = False

        if 'Mon11to12' in request.POST:
            bMon11to12 = True
        else:
            bMon11to12 = False

        if 'Mon12to13' in request.POST:
            bMon12to13 = True
        else:
            bMon12to13 = False

        if 'Mon13to14' in request.POST:
            bMon13to14 = True
        else:
            bMon13to14 = False

        if 'Mon14to15' in request.POST:
            bMon14to15 = True
        else:
            bMon14to15 = False

        if 'Mon15to16' in request.POST:
            bMon15to16 = True
        else:
            bMon15to16 = False

        if 'Mon16to17' in request.POST:
            bMon16to17 = True
        else:
            bMon16to17 = False

        if 'Mon17to18' in request.POST:
            bMon17to18 = True
        else:
            bMon17to18 = False

        if 'Mon18to19' in request.POST:
            bMon18to19 = True
        else:
            bMon18to19 = False

        if 'Mon19to20' in request.POST:
            bMon19to20 = True
        else:
            bMon19to20 = False

        if 'Mon20to21' in request.POST:
            bMon20to21 = True
        else:
            bMon20to21 = False

        if 'Mon21to22' in request.POST:
            bMon21to22 = True
        else:
            bMon21to22 = False

        if 'Mon22to23' in request.POST:
            bMon22to23 = True
        else:
            bMon22to23 = False

        if 'Mon23to0' in request.POST:
            bMon23to0 = True
        else:
            bMon23to0 = False






        if 'Tue0to1' in request.POST:
            bTue0to1 = True
        else:
            bTue0to1 = False

        if 'Tue1to2' in request.POST:
            bTue1to2 = True
        else:
            bTue1to2 = False

        if 'Tue2to3' in request.POST:
            bTue2to3 = True
        else:
            bTue2to3 = False

        if 'Tue3to4' in request.POST:
            bTue3to4 = True
        else:
            bTue3to4 = False

        if 'Tue4to5' in request.POST:
            bTue4to5 = True
        else:
            bTue4to5 = False

        if 'Tue5to6' in request.POST:
            bTue5to6 = True
        else:
            bTue5to6 = False

        if 'Tue6to7' in request.POST:
            bTue6to7 = True
        else:
            bTue6to7 = False

        if 'Tue7to8' in request.POST:
            bTue7to8 = True
        else:
            bTue7to8 = False

        if 'Tue8to9' in request.POST:
            bTue8to9 = True
        else:
            bTue8to9 = False

        if 'Tue9to10' in request.POST:
            bTue9to10 = True
        else:
            bTue9to10 = False

        if 'Tue10to11' in request.POST:
            bTue10to11 = True
        else:
            bTue10to11 = False

        if 'Tue11to12' in request.POST:
            bTue11to12 = True
        else:
            bTue11to12 = False

        if 'Tue12to13' in request.POST:
            bTue12to13 = True
        else:
            bTue12to13 = False

        if 'Tue13to14' in request.POST:
            bTue13to14 = True
        else:
            bTue13to14 = False

        if 'Tue14to15' in request.POST:
            bTue14to15 = True
        else:
            bTue14to15 = False

        if 'Tue15to16' in request.POST:
            bTue15to16 = True
        else:
            bTue15to16 = False

        if 'Tue16to17' in request.POST:
            bTue16to17 = True
        else:
            bTue16to17 = False

        if 'Tue17to18' in request.POST:
            bTue17to18 = True
        else:
            bTue17to18 = False

        if 'Tue18to19' in request.POST:
            bTue18to19 = True
        else:
            bTue18to19 = False

        if 'Tue19to20' in request.POST:
            bTue19to20 = True
        else:
            bTue19to20 = False

        if 'Tue20to21' in request.POST:
            bTue20to21 = True
        else:
            bTue20to21 = False

        if 'Tue21to22' in request.POST:
            bTue21to22 = True
        else:
            bTue21to22 = False

        if 'Tue22to23' in request.POST:
            bTue22to23 = True
        else:
            bTue22to23 = False

        if 'Tue23to0' in request.POST:
            bTue23to0 = True
        else:
            bTue23to0 = False






        if 'Wed0to1' in request.POST:
            bWed0to1 = True
        else:
            bWed0to1 = False

        if 'Wed1to2' in request.POST:
            bWed1to2 = True
        else:
            bWed1to2 = False

        if 'Wed2to3' in request.POST:
            bWed2to3 = True
        else:
            bWed2to3 = False

        if 'Wed3to4' in request.POST:
            bWed3to4 = True
        else:
            bWed3to4 = False

        if 'Wed4to5' in request.POST:
            bWed4to5 = True
        else:
            bWed4to5 = False

        if 'Wed5to6' in request.POST:
            bWed5to6 = True
        else:
            bWed5to6 = False

        if 'Wed6to7' in request.POST:
            bWed6to7 = True
        else:
            bWed6to7 = False

        if 'Wed7to8' in request.POST:
            bWed7to8 = True
        else:
            bWed7to8 = False

        if 'Wed8to9' in request.POST:
            bWed8to9 = True
        else:
            bWed8to9 = False

        if 'Wed9to10' in request.POST:
            bWed9to10 = True
        else:
            bWed9to10 = False

        if 'Wed10to11' in request.POST:
            bWed10to11 = True
        else:
            bWed10to11 = False

        if 'Wed11to12' in request.POST:
            bWed11to12 = True
        else:
            bWed11to12 = False

        if 'Wed12to13' in request.POST:
            bWed12to13 = True
        else:
            bWed12to13 = False

        if 'Wed13to14' in request.POST:
            bWed13to14 = True
        else:
            bWed13to14 = False

        if 'Wed14to15' in request.POST:
            bWed14to15 = True
        else:
            bWed14to15 = False

        if 'Wed15to16' in request.POST:
            bWed15to16 = True
        else:
            bWed15to16 = False

        if 'Wed16to17' in request.POST:
            bWed16to17 = True
        else:
            bWed16to17 = False

        if 'Wed17to18' in request.POST:
            bWed17to18 = True
        else:
            bWed17to18 = False

        if 'Wed18to19' in request.POST:
            bWed18to19 = True
        else:
            bWed18to19 = False

        if 'Wed19to20' in request.POST:
            bWed19to20 = True
        else:
            bWed19to20 = False

        if 'Wed20to21' in request.POST:
            bWed20to21 = True
        else:
            bWed20to21 = False

        if 'Wed21to22' in request.POST:
            bWed21to22 = True
        else:
            bWed21to22 = False

        if 'Wed22to23' in request.POST:
            bWed22to23 = True
        else:
            bWed22to23 = False

        if 'Wed23to0' in request.POST:
            bWed23to0 = True
        else:
            bWed23to0 = False


        if 'Thu0to1' in request.POST:
            bThu0to1 = True
        else:
            bThu0to1 = False

        if 'Thu1to2' in request.POST:
            bThu1to2 = True
        else:
            bThu1to2 = False

        if 'Thu2to3' in request.POST:
            bThu2to3 = True
        else:
            bThu2to3 = False

        if 'Thu3to4' in request.POST:
            bThu3to4 = True
        else:
            bThu3to4 = False

        if 'Thu4to5' in request.POST:
            bThu4to5 = True
        else:
            bThu4to5 = False

        if 'Thu5to6' in request.POST:
            bThu5to6 = True
        else:
            bThu5to6 = False

        if 'Thu6to7' in request.POST:
            bThu6to7 = True
        else:
            bThu6to7 = False

        if 'Thu7to8' in request.POST:
            bThu7to8 = True
        else:
            bThu7to8 = False

        if 'Thu8to9' in request.POST:
            bThu8to9 = True
        else:
            bThu8to9 = False

        if 'Thu9to10' in request.POST:
            bThu9to10 = True
        else:
            bThu9to10 = False

        if 'Thu10to11' in request.POST:
            bThu10to11 = True
        else:
            bThu10to11 = False

        if 'Thu11to12' in request.POST:
            bThu11to12 = True
        else:
            bThu11to12 = False

        if 'Thu12to13' in request.POST:
            bThu12to13 = True
        else:
            bThu12to13 = False

        if 'Thu13to14' in request.POST:
            bThu13to14 = True
        else:
            bThu13to14 = False

        if 'Thu14to15' in request.POST:
            bThu14to15 = True
        else:
            bThu14to15 = False

        if 'Thu15to16' in request.POST:
            bThu15to16 = True
        else:
            bThu15to16 = False

        if 'Thu16to17' in request.POST:
            bThu16to17 = True
        else:
            bThu16to17 = False

        if 'Thu17to18' in request.POST:
            bThu17to18 = True
        else:
            bThu17to18 = False

        if 'Thu18to19' in request.POST:
            bThu18to19 = True
        else:
            bThu18to19 = False

        if 'Thu19to20' in request.POST:
            bThu19to20 = True
        else:
            bThu19to20 = False

        if 'Thu20to21' in request.POST:
            bThu20to21 = True
        else:
            bThu20to21 = False

        if 'Thu21to22' in request.POST:
            bThu21to22 = True
        else:
            bThu21to22 = False

        if 'Thu22to23' in request.POST:
            bThu22to23 = True
        else:
            bThu22to23 = False

        if 'Thu23to0' in request.POST:
            bThu23to0 = True
        else:
            bThu23to0 = False




        if 'Fri0to1' in request.POST:
            bFri0to1 = True
        else:
            bFri0to1 = False

        if 'Fri1to2' in request.POST:
            bFri1to2 = True
        else:
            bFri1to2 = False

        if 'Fri2to3' in request.POST:
            bFri2to3 = True
        else:
            bFri2to3 = False

        if 'Fri3to4' in request.POST:
            bFri3to4 = True
        else:
            bFri3to4 = False

        if 'Fri4to5' in request.POST:
            bFri4to5 = True
        else:
            bFri4to5 = False

        if 'Fri5to6' in request.POST:
            bFri5to6 = True
        else:
            bFri5to6 = False

        if 'Fri6to7' in request.POST:
            bFri6to7 = True
        else:
            bFri6to7 = False

        if 'Fri7to8' in request.POST:
            bFri7to8 = True
        else:
            bFri7to8 = False

        if 'Fri8to9' in request.POST:
            bFri8to9 = True
        else:
            bFri8to9 = False

        if 'Fri9to10' in request.POST:
            bFri9to10 = True
        else:
            bFri9to10 = False

        if 'Fri10to11' in request.POST:
            bFri10to11 = True
        else:
            bFri10to11 = False

        if 'Fri11to12' in request.POST:
            bFri11to12 = True
        else:
            bFri11to12 = False

        if 'Fri12to13' in request.POST:
            bFri12to13 = True
        else:
            bFri12to13 = False

        if 'Fri13to14' in request.POST:
            bFri13to14 = True
        else:
            bFri13to14 = False

        if 'Fri14to15' in request.POST:
            bFri14to15 = True
        else:
            bFri14to15 = False

        if 'Fri15to16' in request.POST:
            bFri15to16 = True
        else:
            bFri15to16 = False

        if 'Fri16to17' in request.POST:
            bFri16to17 = True
        else:
            bFri16to17 = False

        if 'Fri17to18' in request.POST:
            bFri17to18 = True
        else:
            bFri17to18 = False

        if 'Fri18to19' in request.POST:
            bFri18to19 = True
        else:
            bFri18to19 = False

        if 'Fri19to20' in request.POST:
            bFri19to20 = True
        else:
            bFri19to20 = False

        if 'Fri20to21' in request.POST:
            bFri20to21 = True
        else:
            bFri20to21 = False

        if 'Fri21to22' in request.POST:
            bFri21to22 = True
        else:
            bFri21to22 = False

        if 'Fri22to23' in request.POST:
            bFri22to23 = True
        else:
            bFri22to23 = False

        if 'Fri23to0' in request.POST:
            bFri23to0 = True
        else:
            bFri23to0 = False


        if 'Sat0to1' in request.POST:
            bSat0to1 = True
        else:
            bSat0to1 = False

        if 'Sat1to2' in request.POST:
            bSat1to2 = True
        else:
            bSat1to2 = False

        if 'Sat2to3' in request.POST:
            bSat2to3 = True
        else:
            bSat2to3 = False

        if 'Sat3to4' in request.POST:
            bSat3to4 = True
        else:
            bSat3to4 = False

        if 'Sat4to5' in request.POST:
            bSat4to5 = True
        else:
            bSat4to5 = False

        if 'Sat5to6' in request.POST:
            bSat5to6 = True
        else:
            bSat5to6 = False

        if 'Sat6to7' in request.POST:
            bSat6to7 = True
        else:
            bSat6to7 = False

        if 'Sat7to8' in request.POST:
            bSat7to8 = True
        else:
            bSat7to8 = False

        if 'Sat8to9' in request.POST:
            bSat8to9 = True
        else:
            bSat8to9 = False

        if 'Sat9to10' in request.POST:
            bSat9to10 = True
        else:
            bSat9to10 = False

        if 'Sat10to11' in request.POST:
            bSat10to11 = True
        else:
            bSat10to11 = False

        if 'Sat11to12' in request.POST:
            bSat11to12 = True
        else:
            bSat11to12 = False

        if 'Sat12to13' in request.POST:
            bSat12to13 = True
        else:
            bSat12to13 = False

        if 'Sat13to14' in request.POST:
            bSat13to14 = True
        else:
            bSat13to14 = False

        if 'Sat14to15' in request.POST:
            bSat14to15 = True
        else:
            bSat14to15 = False

        if 'Sat15to16' in request.POST:
            bSat15to16 = True
        else:
            bSat15to16 = False

        if 'Sat16to17' in request.POST:
            bSat16to17 = True
        else:
            bSat16to17 = False

        if 'Sat17to18' in request.POST:
            bSat17to18 = True
        else:
            bSat17to18 = False

        if 'Sat18to19' in request.POST:
            bSat18to19 = True
        else:
            bSat18to19 = False

        if 'Sat19to20' in request.POST:
            bSat19to20 = True
        else:
            bSat19to20 = False

        if 'Sat20to21' in request.POST:
            bSat20to21 = True
        else:
            bSat20to21 = False

        if 'Sat21to22' in request.POST:
            bSat21to22 = True
        else:
            bSat21to22 = False

        if 'Sat22to23' in request.POST:
            bSat22to23 = True
        else:
            bSat22to23 = False

        if 'Sat23to0' in request.POST:
            bSat23to0 = True
        else:
            bSat23to0 = False



        if 'Sun0to1' in request.POST:
            bSun0to1 = True
        else:
            bSun0to1 = False

        if 'Sun1to2' in request.POST:
            bSun1to2 = True
        else:
            bSun1to2 = False

        if 'Sun2to3' in request.POST:
            bSun2to3 = True
        else:
            bSun2to3 = False

        if 'Sun3to4' in request.POST:
            bSun3to4 = True
        else:
            bSun3to4 = False

        if 'Sun4to5' in request.POST:
            bSun4to5 = True
        else:
            bSun4to5 = False

        if 'Sun5to6' in request.POST:
            bSun5to6 = True
        else:
            bSun5to6 = False

        if 'Sun6to7' in request.POST:
            bSun6to7 = True
        else:
            bSun6to7 = False

        if 'Sun7to8' in request.POST:
            bSun7to8 = True
        else:
            bSun7to8 = False

        if 'Sun8to9' in request.POST:
            bSun8to9 = True
        else:
            bSun8to9 = False

        if 'Sun9to10' in request.POST:
            bSun9to10 = True
        else:
            bSun9to10 = False

        if 'Sun10to11' in request.POST:
            bSun10to11 = True
        else:
            bSun10to11 = False

        if 'Sun11to12' in request.POST:
            bSun11to12 = True
        else:
            bSun11to12 = False

        if 'Sun12to13' in request.POST:
            bSun12to13 = True
        else:
            bSun12to13 = False

        if 'Sun13to14' in request.POST:
            bSun13to14 = True
        else:
            bSun13to14 = False

        if 'Sun14to15' in request.POST:
            bSun14to15 = True
        else:
            bSun14to15 = False

        if 'Sun15to16' in request.POST:
            bSun15to16 = True
        else:
            bSun15to16 = False

        if 'Sun16to17' in request.POST:
            bSun16to17 = True
        else:
            bSun16to17 = False

        if 'Sun17to18' in request.POST:
            bSun17to18 = True
        else:
            bSun17to18 = False

        if 'Sun18to19' in request.POST:
            bSun18to19 = True
        else:
            bSun18to19 = False

        if 'Sun19to20' in request.POST:
            bSun19to20 = True
        else:
            bSun19to20 = False

        if 'Sun20to21' in request.POST:
            bSun20to21 = True
        else:
            bSun20to21 = False

        if 'Sun21to22' in request.POST:
            bSun21to22 = True
        else:
            bSun21to22 = False

        if 'Sun22to23' in request.POST:
            bSun22to23 = True
        else:
            bSun22to23 = False

        if 'Sun23to0' in request.POST:
            bSun23to0 = True
        else:
            bSun23to0 = False

        mon = Day.objects.create(
            h0to1 = bMon0to1,
            h1to2 = bMon1to2,
            h2to3 = bMon2to3,
            h3to4 = bMon3to4,
            h4to5 = bMon4to5,
            h5to6 = bMon5to6,
            h6to7 = bMon6to7,
            h7to8 = bMon7to8,
            h8to9 = bMon8to9,
            h9to10 = bMon9to10,
            h10to11 = bMon10to11,
            h11to12 = bMon11to12,
            h12to13 = bMon12to13,
            h13to14 = bMon13to14,
            h14to15 = bMon14to15,
            h15to16 = bMon15to16,
            h16to17 = bMon16to17,
            h17to18 = bMon17to18,
            h18to19 = bMon18to19,
            h19to20 = bMon19to20,
            h20to21 = bMon20to21,
            h21to22 = bMon21to22,
            h22to23 = bMon22to23,
            h23to0 = bMon23to0
        )
        tue = Day.objects.create(
            h0to1 = bTue0to1,
            h1to2 = bTue1to2,
            h2to3 = bTue2to3,
            h3to4 = bTue3to4,
            h4to5 = bTue4to5,
            h5to6 = bTue5to6,
            h6to7 = bTue6to7,
            h7to8 = bTue7to8,
            h8to9 = bTue8to9,
            h9to10 = bTue9to10,
            h10to11 = bTue10to11,
            h11to12 = bTue11to12,
            h12to13 = bTue12to13,
            h13to14 = bTue13to14,
            h14to15 = bTue14to15,
            h15to16 = bTue15to16,
            h16to17 = bTue16to17,
            h17to18 = bTue17to18,
            h18to19 = bTue18to19,
            h19to20 = bTue19to20,
            h20to21 = bTue20to21,
            h21to22 = bTue21to22,
            h22to23 = bTue22to23,
            h23to0 = bTue23to0
        )
        wed = Day.objects.create(
            h0to1 = bWed0to1,
            h1to2 = bWed1to2,
            h2to3 = bWed2to3,
            h3to4 = bWed3to4,
            h4to5 = bWed4to5,
            h5to6 = bWed5to6,
            h6to7 = bWed6to7,
            h7to8 = bWed7to8,
            h8to9 = bWed8to9,
            h9to10 = bWed9to10,
            h10to11 = bWed10to11,
            h11to12 = bWed11to12,
            h12to13 = bWed12to13,
            h13to14 = bWed13to14,
            h14to15 = bWed14to15,
            h15to16 = bWed15to16,
            h16to17 = bWed16to17,
            h17to18 = bWed17to18,
            h18to19 = bWed18to19,
            h19to20 = bWed19to20,
            h20to21 = bWed20to21,
            h21to22 = bWed21to22,
            h22to23 = bWed22to23,
            h23to0 = bWed23to0
        )
        thu = Day.objects.create(
            h0to1 = bThu0to1,
            h1to2 = bThu1to2,
            h2to3 = bThu2to3,
            h3to4 = bThu3to4,
            h4to5 = bThu4to5,
            h5to6 = bThu5to6,
            h6to7 = bThu6to7,
            h7to8 = bThu7to8,
            h8to9 = bThu8to9,
            h9to10 = bThu9to10,
            h10to11 = bThu10to11,
            h11to12 = bThu11to12,
            h12to13 = bThu12to13,
            h13to14 = bThu13to14,
            h14to15 = bThu14to15,
            h15to16 = bThu15to16,
            h16to17 = bThu16to17,
            h17to18 = bThu17to18,
            h18to19 = bThu18to19,
            h19to20 = bThu19to20,
            h20to21 = bThu20to21,
            h21to22 = bThu21to22,
            h22to23 = bThu22to23,
            h23to0 = bThu23to0
        )
        fri = Day.objects.create(
            h0to1 = bFri0to1,
            h1to2 = bFri1to2,
            h2to3 = bFri2to3,
            h3to4 = bFri3to4,
            h4to5 = bFri4to5,
            h5to6 = bFri5to6,
            h6to7 = bFri6to7,
            h7to8 = bFri7to8,
            h8to9 = bFri8to9,
            h9to10 = bFri9to10,
            h10to11 = bFri10to11,
            h11to12 = bFri11to12,
            h12to13 = bFri12to13,
            h13to14 = bFri13to14,
            h14to15 = bFri14to15,
            h15to16 = bFri15to16,
            h16to17 = bFri16to17,
            h17to18 = bFri17to18,
            h18to19 = bFri18to19,
            h19to20 = bFri19to20,
            h20to21 = bFri20to21,
            h21to22 = bFri21to22,
            h22to23 = bFri22to23,
            h23to0 = bFri23to0
        )
        sat = Day.objects.create(
            h0to1 = bSat0to1,
            h1to2 = bSat1to2,
            h2to3 = bSat2to3,
            h3to4 = bSat3to4,
            h4to5 = bSat4to5,
            h5to6 = bSat5to6,
            h6to7 = bSat6to7,
            h7to8 = bSat7to8,
            h8to9 = bSat8to9,
            h9to10 = bSat9to10,
            h10to11 = bSat10to11,
            h11to12 = bSat11to12,
            h12to13 = bSat12to13,
            h13to14 = bSat13to14,
            h14to15 = bSat14to15,
            h15to16 = bSat15to16,
            h16to17 = bSat16to17,
            h17to18 = bSat17to18,
            h18to19 = bSat18to19,
            h19to20 = bSat19to20,
            h20to21 = bSat20to21,
            h21to22 = bSat21to22,
            h22to23 = bSat22to23,
            h23to0 = bSat23to0
        )
        sun = Day.objects.create(
            h0to1 = bSun0to1,
            h1to2 = bSun1to2,
            h2to3 = bSun2to3,
            h3to4 = bSun3to4,
            h4to5 = bSun4to5,
            h5to6 = bSun5to6,
            h6to7 = bSun6to7,
            h7to8 = bSun7to8,
            h8to9 = bSun8to9,
            h9to10 = bSun9to10,
            h10to11 = bSun10to11,
            h11to12 = bSun11to12,
            h12to13 = bSun12to13,
            h13to14 = bSun13to14,
            h14to15 = bSun14to15,
            h15to16 = bSun15to16,
            h16to17 = bSun16to17,
            h17to18 = bSun17to18,
            h18to19 = bSun18to19,
            h19to20 = bSun19to20,
            h20to21 = bSun20to21,
            h21to22 = bSun21to22,
            h22to23 = bSun22to23,
            h23to0 = bSun23to0
        )
        active_user = User.objects.get(id = request.session['active_user_id'])
        schedule = Schedule.objects.get(user = active_user)
        schedule.mon = mon
        schedule.tue = tue
        schedule.wed = wed
        schedule.thu = thu
        schedule.fri = fri
        schedule.sat = sat
        schedule.sun = sun
        schedule.save()

    return redirect(reverse('user_profile:edit_profile', kwargs={'user_id': request.session['active_user_id']}))

def edit_profile(request, user_id):
    user_id = request.session.get('active_user_id')
    form = ImgForm()
    data = {
        "user" : User.objects.get(id=user_id),
        'form' : form,
        'img' : Images.objects.filter(user_id = user_id)
        }
    if request.method == "POST":
        user_id = request.session.get('active_user_id')

        uSt = request.POST['street_number']
        uRoute = request.POST['route']
        uCity = request.POST['city']
        uState = request.POST['state']

        url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ uSt + ','+ uRoute + ',' + uCity + ',' + uState +'&key=AIzaSyBj4eaE79fE1cqdaq1XZALhzxCpKPd2F2I'
        headers={"X-Mashape-Key": "ABCDEFG12345"}
        response = unirest.get(url, headers=headers)
        data = response.body
        longtitude = data["results"][0]["geometry"]["location"]["lng"]
        latitude = data["results"][0]["geometry"]["location"]["lat"]

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
            longtitude = longtitude,
            latitude = latitude,
            about_me = request.POST['about_me']
        )

        return redirect(reverse('user_profile:index', kwargs={'user_id': user_id}))

    return render(request, 'user_profile/edit_profile.html', data)
