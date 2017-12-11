from django.contrib import admin

from .models import Course, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]

class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'type']

admin.site.register(Course, CourseAdmin)
admin.site.register(Membership, MembershipAdmin)
