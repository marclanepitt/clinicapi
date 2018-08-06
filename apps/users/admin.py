from django.contrib import admin

from .models import StaffUser


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(StaffUser)
