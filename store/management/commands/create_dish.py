from django.core.management.base import BaseCommand, CommandError
from store.models import Dish


class Command(BaseCommand):
    help = "Create only one dish"

    def handle(self, *args, **options):
        Dish.objects.create(
            name="Pizza",
            description="BEST Pizza",
            price=100,
        )
