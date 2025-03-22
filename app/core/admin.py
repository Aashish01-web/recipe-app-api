"""
Customisation for admin
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Customize admin page"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        (_('Permissions'), {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        (_('Important Dates'), {
            "fields": (
                'last_login',
            )
        }),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

    @admin.action(description="Mark selected users as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected users as inactive")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    actions = [make_active, make_inactive]


admin.site.register(models.User, UserAdmin)

admin.site.site_header = "Resort Management Admin"
admin.site.site_title = "Resort Admin Portal"
admin.site.index_title = "Welcome to the Resort Control Panel"
