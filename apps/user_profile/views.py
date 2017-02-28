from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User, UserManager, Profile
from ..schedules.models import Schedule

def index(request, user_id):
    user_id = request.session.get('active_user_id')

    data = {
        "user" : User.objects.get(id=user_id),
        }

    return render(request, 'user_profile/index.html', data)

def view_times(request):
    context = {
    'schedule': Schedule.objects.get(user = request.session['active_user_id'])
    }
    return render(request, 'user_profile/edit_times.html', context)

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
