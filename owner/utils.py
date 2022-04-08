from django.db import connection
from .models import Tenant


def hostname_from_request(request):
    # split on `:` to remove port
    # TODO : Using something like django hosts to get subdomain (www, tenant-1..)
    return request.get_host().split(':')[0].lower()


def tenant_schema_from_request(request):
    hostname = hostname_from_request(request)
    default_tenant = "public"
    tenants = Tenant.objects.using('default').all()
    tenant_filter = tenants.filter(subdomain=hostname)
    if tenant_filter.exists():
        return tenant_filter.first().schema
    else:
        return default_tenant

def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_tenant_schema_for_request(request)
        response = self.get_response(request)
        return response
