from django.core.management import BaseCommand
from .champ_class_create_bace.bard.base import create_bard_base
from .champ_class_create_bace.bard.arch_one import arch_one, arch_two


class Command(BaseCommand):
    help = 'Добавление заклинаний'

    def handle(self, *args, **options):
        bard = create_bard_base()
        arch_one(bard)
        arch_two(bard)


