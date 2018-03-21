from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Member, Attention, Invitation, Area
# Register your models here.



class memberAdmin(admin.ModelAdmin):
    pass


class attentionAdmin(admin.ModelAdmin):
    pass

class invitationAdmin(admin.ModelAdmin):
    pass

class areaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Member, memberAdmin)
admin.site.register(Attention, attentionAdmin)
admin.site.register(Invitation, invitationAdmin)
admin.site.register(Area, areaAdmin)