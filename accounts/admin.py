from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from accounts.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('gender', 'is_staff', 'is_superuser', 'is_active')

    search_fields = ('username', 'email', 'phone', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender', 'age', 'description')}),
        ('Contact info', {'fields': ('phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # fieldsets = (
    #     ('Personal Info', {'fields': ('first_name', 'last_name', 'email', '', '', 'age', '', 'description')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    # )

    list_editable = ('is_staff', 'is_active')
    list_per_page = 20

    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Mark selected users as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Mark selected users as inactive"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Or any custom display
