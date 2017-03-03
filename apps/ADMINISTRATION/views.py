from django.shortcuts import render
from ..login_register.models import User, UserManager
from ..user_profile.models import Profile, Match, Images
from ..schedules.models import Schedule, Day
# Create your views here.
def index(request):
    context = {
    'users': User.objects.all(),
    
    }
    return render(request, 'ADMINISTRATION/index.html', context)
