from django.shortcuts import render, redirect
from ..login_register.models import User, UserManager
from ..user_profile.models import Profile, Match, Images
from ..schedules.models import Schedule, Day
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context = {
    'users': User.objects.all(),
    }
    return render(request, 'ADMINISTRATION/index.html', context)

def ADMIN_edit(request, user_id):
    user = User.objects.get(id = user_id)
    if Profile.objects.filter(user = user):
        context = {
        'user': user,
        'profile': Profile.objects.get(user = user)
        }
    else:
        context = {
        'user': user
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
