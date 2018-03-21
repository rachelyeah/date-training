import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from registration import signals
from registration.views import RegistrationView as BaseRegistrationView
from .models import Member, Attention, Invitation
from .forms import ProfileForm

# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationView(BaseRegistrationView):
    """
    Registration via the simplest possible process: a user supplies a
    username, email address and password (the bare minimum for a
    useful account), and is immediately signed up and logged in.
    """
    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/'


def index(request):
    return render(request, 'dating/index.html')



@login_required
def profile(request):
    user = request.user
    members = Member.objects.filter(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            if len(members) == 0:
                Member.objects.create(user=user,
                                      username=form.cleaned_data['username'],
                                      phone=form.cleaned_data['phone'],
                                      gender=form.cleaned_data['gender'],
                                      age=form.cleaned_data['age'])
            else:
                member = members[0]
                member.username = form.cleaned_data['username']
                member.phone = form.cleaned_data['phone']
                member.gender = form.cleaned_data['gender']
                member.age = form.cleaned_data['age']
                member.save()

            return HttpResponseRedirect('/home/')
        else:
            return render(request, 'dating/profile.html')

    else:
        form = ProfileForm()
        context = {'form': form, 'member': None if len(members) == 0 else members[0]}
        return render(request, 'dating/profile.html', context)


@login_required
def home(request):
    user = request.user
    members = Member.objects.filter(user=user)
    if len(members) == 0:
        context = {'member': None, 'fo': 0, 'username': user}
    else:
        fo = Attention.objects.filter(follower=members[0]).count()
        context = {'member': members[0], 'fo': fo, 'username': user}
    return render(request, 'dating/home.html', context)



@login_required
def attention(request):
    user = request.user
    members = Member.objects.filter(user=user)
    if len(members) == 0:
        context = {'following': []}
    else:
        followers = Attention.objects.filter(follower=user).select_related('befollowed')
        member_id = Member.objects.filter(user=followers)
        context = {'following': followers, 'member_id': member_id}
    return render(request, 'dating/attention.html', context)

@login_required
def upage(request, member_id):
    member = Member.object(member_id).username
    context = {'member': member}
    return render(request, 'dating/upage.html', context)




@login_required
def invitation(request):
    user = request.user
    invitees = Invitation.objects.filter(invitee=user)
    context = {'invitees': invitees}
    return render(request, 'dating/invitees.html', context)