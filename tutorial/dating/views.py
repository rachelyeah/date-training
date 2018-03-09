import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Member, Attention, Invitation
from .forms import ProfileForm

# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()




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

            return HttpResponseRedirect('dating/home/')
        else:
            return render(request, 'dating/profile.html')

    else:
        form = ProfileForm()
        context = {'form':form, 'members': None if len(members) == 0 else members[0]}
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
    followers = Attention.objects.filter(followers=user)
    context = {'followers': followers}
    return render(request, 'dating/attention.html', context)


@login_required
def invitation(request):
    user = request.user
    invitees = Invitation.objects.filter(invitee=user)
    context = {'invitees': invitees}
    return render(request, 'dating/invitees.html', context)