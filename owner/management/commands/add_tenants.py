from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection
from owner.models import Tenant


class Command(MigrationCommand):
    def handle(self, *args, **options):
        tenants = Tenant.objects.using('default').all()
        with connection.cursor() as cursor:
            schemas = tenants.values_list('schema', flat=True).distinct()
            for schema in schemas:
                print("Adding schema", schema)
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
                cursor.execute(f"SET search_path to {schema}")
                super(Command, self).handle(*args, **options)
