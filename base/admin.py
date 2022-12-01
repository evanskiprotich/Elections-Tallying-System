from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Result, Candidate

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


class ResultAdmin(admin.ModelAdmin):
    model = Result
    list_display = ["officer",  "candidate_one", "candidate_two", "candidate_three", "candidate_four", "totalvotes", "rejectedvotes", "validvotes", "regvoters"]

    # def get_officer(self, obj):
    #     return obj.officer.name
    # get_officer.admin_order_field  = 'officer'  
admin.site.register(Result, ResultAdmin)


class CandidatesAdmin(admin.ModelAdmin):
    model = Candidate
    list_display = ["candidate_name", "candidate_image", "candidate_party", "party_logo",]

    def get_candidate(self, obj):
        return obj.candidate.name
    get_candidate.admin_order_field  = 'candidate'  
admin.site.register(Candidate, CandidatesAdmin)
