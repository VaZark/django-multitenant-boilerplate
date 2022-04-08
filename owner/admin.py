from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Organisation, Tenant

class TenantInline(admin.TabularInline):
    model = Tenant
    extra = 0
    can_delete = False
    
    def has_add_permission(self, request, obj=None, **kwargs):
        return False
    

    def has_change_permission(self, request, obj=None, **kwargs):
        return False


class ClientInline(admin.TabularInline):
    model = Client
    extra = 0
    fields = ['username', 'first_name', 'last_name', 'is_active', 'last_login']
    show_change_link = True
    can_delete = False

    def has_add_permission(self, request, obj=None, **kwargs):
        return False
    

    def has_change_permission(self, request, obj=None, **kwargs):
        return False

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    inlines = [TenantInline, ClientInline]


@admin.register(Tenant)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(UserAdmin):
    pass