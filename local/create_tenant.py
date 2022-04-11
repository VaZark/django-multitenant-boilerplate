from owner.models import Domain, Tenant

# create your public tenant
tenant = Tenant(
    organisation=None,
    tenant_type="crm",
    name="FLOA",
    schema_name="floa_crm",
)

tenant.save()

# Add one or more domains for the tenant
# don't add your port or www on domain field! on a local server you'll want to use localhost here
domain = Domain(
    domain = "floa.localhost" ,
    tenant = tenant,
    is_primary = True
)
domain.save()
