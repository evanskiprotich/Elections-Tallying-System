from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, ElectionResult

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)


class ElectionResultAdmin(admin.ModelAdmin):
    model = ElectionResult
    list_display = ["officer","candidate_one", "candidate_two", "candidate_three", "candidate_four", ]

    def get_officer(self, obj):
        return obj.officer.name
    get_officer.admin_order_field  = 'officer'  
admin.site.register(ElectionResult, ElectionResultAdmin)