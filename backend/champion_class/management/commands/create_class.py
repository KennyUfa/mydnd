from django.core.management import BaseCommand
from .champ_class_create_bace.bard.base import create_bard_base
from .champ_class_create_bace.bard.arch_one import arch_one, arch_two

from .champ_class_create_bace.legolas_create.leg_base import create_archer_base
from .champ_class_create_bace.var.var_base import create_var_base
from .champ_class_create_bace.varavar.varvar_base import create_varvar
from .champ_class_create_bace.mage.mage_base import create_mage
from .champ_class_create_bace.monah.monah_base import create_monah
from .champ_class_create_bace.priest.priest_base import create_cleric
from .champ_class_create_bace.rogue.rogue_base import create_rogue



class Command(BaseCommand):
    help = 'Добавление заклинаний'

    def handle(self, *args, **options):
        bard = create_bard_base()
        arch_one(bard)
        arch_two(bard)
        archer = create_archer_base()
        var = create_var_base()
        varvar = create_varvar()
        mage = create_mage()
        monah = create_monah()
        cleric = create_cleric()
        rogue = create_rogue()