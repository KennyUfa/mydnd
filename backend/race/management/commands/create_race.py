from django.core.management import BaseCommand

from .races.little import little
from .races.human import human
from .races.half_elf import half_elf


class Command(BaseCommand):
    def handle(self, *args, **options):
        little()
        human()
        half_elf()
