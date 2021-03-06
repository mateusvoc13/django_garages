from django.core.management.base import BaseCommand
from directory.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin = 'admin'
        email = 'email@email.com'

        if not User.objects.filter(id=1):
            admin = User.objects.create_superuser(name="Mateus",
                                                  username=admin,
                                                  email=email,
                                                  password=admin)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
