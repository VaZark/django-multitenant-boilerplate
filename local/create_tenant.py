from owner.models import Domain, Tenant

# create your public tenant
tenant = Tenant(
    organisation=None,
    tenant_type="crm",
    name="Simplicar",
    schema_name="simplicar_crm",
)

tenant.save()

# Add one or more domains for the tenant
# don't add your port or www on domain field! on a local server you'll want to use localhost here
domain = Domain(
    domain = "simplicar.localhost" ,
    tenant = tenant,
    is_primary = True
)
domain.save()

# python manage.py create_tenant --domain-domain=floa.localhost --schema_name=floa --name=floa