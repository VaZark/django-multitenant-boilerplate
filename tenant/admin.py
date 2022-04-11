from django.contrib import admin

from tenant.models import DemandePret

# Register your models here.

class TenantAdmin(admin.AdminSite):
    site_header = "Tenant admin"
    site_title = "Tenant Admin Portal"
    index_title = "DB Admin"

tenant_admin = TenantAdmin(name='tenant_admin')

class DemandePretAdmin(admin.ModelAdmin):
    pass

tenant_admin.register(DemandePret, DemandePretAdmin)