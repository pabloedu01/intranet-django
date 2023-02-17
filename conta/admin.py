from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AccountInline(admin.StackedInline):
    model = conta
    can_delete = False
    verbose_name_plural = 'contas'

class CustomUserAdmin (UserAdmin):
    inlines = (AccountInline,)

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
admin.site.register(conta)