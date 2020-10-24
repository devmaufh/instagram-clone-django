from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin """
    list_display_links = ('pk', 'user')
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number',
        'website',
        'pk'
    )
    list_filter = (
        'user__is_active',
        'created_at',
        'updated_at'
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography',)
            )
        }),
        ('Meta', {
            'fields': (('created_at', 'updated_at'),)
        })
    )
    readonly_fields = ('created_at', 'updated_at')


class ProfileInLine(admin.StackedInline):
    """ Profile in line Admin for users """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin. """
    inlines = (ProfileInLine,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
