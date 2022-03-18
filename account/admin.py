from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

UserAdmin.fieldsets += (
    ('fd', {'fields': ('special_user','is_verify','shortdes','content','image','slug','rate')}),
)

UserAdmin.list_display += ('Is_special_user','is_verify')

admin.site.register(User, UserAdmin)
