from django.shortcuts import render, redirect
from ..login_register.models import User, UserManager
from ..user_profile.models import Profile, Match, Images
from ..schedules.models import Schedule, Day
from django.core.urlresolvers import reverse
from ..user_profile.forms import ImgForm
from PIL import Image

# Create your views here.
def index(request):
    context = {
    'users': User.objects.all(),
    }
    return render(request, 'ADMINISTRATION/index.html', context)

def ADMIN_edit(request, user_id):
    user = User.objects.get(id = user_id)
    form = ImgForm()
    if Profile.objects.filter(user = user):
        context = {
        'user': user,
        'profile': Profile.objects.get(user = user),
        'img': Images.objects.filter(user_id = user_id),
        'form' : form
        }
    else:
        context = {
        'user': user,
        'img': Images.objects.filter(user_id = user_id),
        'form' : form
        }
    return render(request, 'ADMINISTRATION/ADMIN_edit.html', context)

def ADMIN_delete(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect(reverse('admin:index'))

def ADMIN_save(request, user_id):
    user = User.objects.get(id = user_id)
    if Profile.objects.filter(user = user):
        profile = Profile.objects.get(user = user)
    if request.method == 'POST':
        newFName = request.POST['fname']
        newLName = request.POST['lname']
        newEmail = request.POST['email']
        if Profile.objects.filter(user = user):
            newOcc = request.POST['occupation']
            newComp = request.POST['company']

        user.firstname = newFName
        user.lastname = newLName
        user.Email = newEmail
        user.save()
        if Profile.objects.filter(user = user):
            profile.occupation = newOcc
            profile.company = newComp
            profile.save()
    return redirect(reverse('admin:index'))

def ADMIN_makeadmin(request, user_id):
    user = User.objects.get(id = user_id)
    user.userLevel = True
    user.save()
    return redirect(reverse('admin:index'))

def ADMIN_changeimage(request, user_id):
    image = Images.objects.only('avatar').get(user_id = user_id).avatar
    im = Image.open(image)
    if im.size[0] > 750:
        basewidth = 750
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        strhsize = str(hsize) + 'px'
        context = {
        'img': Images.objects.filter(user_id = user_id),
        'user': User.objects.get(id = user_id),
        'size': strhsize
        }
    else:
        context = {
        'img': Images.objects.filter(user_id = user_id),
        'user': User.objects.get(id = user_id)
        }
    return render(request, 'ADMINISTRATION/image_resize.html', context)
def ADMIN_image(request, user_id):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            delete = Images.objects.filter(user = user_id).delete()
            update = Images.objects.filter(user = user_id).create(avatar=request.FILES['imgfile'], user_id = user_id, resize = False)
    return redirect(reverse('admin:ADMIN_changeimage', kwargs={'user_id': user_id}))

def ADMIN_resize(request, user_id):
    user = str(user_id)
    right = float(request.POST['cropx'])
    down = float(request.POST['cropy'])
    image = Images.objects.only('avatar').get(user_id = user_id).avatar
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
    user_id = user_id
    delete = Images.objects.filter(user = user_id).delete()
    update = Images.objects.filter(user = user_id).create(avatar = location, user_id = user_id, resize = True)
    return redirect(reverse('admin:ADMIN_edit', kwargs={'user_id': user_id}))
