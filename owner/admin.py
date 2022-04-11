from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Organisation, Tenant


class TenantInline(admin.TabularInline):
    model = Tenant
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None, **kwargs):
        return False

    def has_change_permission(self, request, obj=None, **kwargs):
        return False


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    inlines = [TenantInline]


@admin.register(Tenant)
class ClientAdmin(admin.ModelAdmin):
    pass
