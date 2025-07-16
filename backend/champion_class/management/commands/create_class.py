from django.core.management import BaseCommand

from .champ_class_create_bace.artificer.artificer_base import create_artif
from .champ_class_create_bace.bard.arch_one import arch_one, arch_two
from .champ_class_create_bace.bard.base import create_bard_base
from .champ_class_create_bace.kold.kold_base import create_kold_base
from .champ_class_create_bace.legolas_create.leg_base import create_archer_base
from .champ_class_create_bace.mage.mage_base import create_mage
from .champ_class_create_bace.monah.monah_base import create_monah
from .champ_class_create_bace.priest.priest_base import create_cleric
from .champ_class_create_bace.rogue.rogue_base import create_rogue
from .champ_class_create_bace.sorcerer.sorcerer_base import create_sorcerer
from .champ_class_create_bace.var.var_base import create_var_base
from .champ_class_create_bace.varavar.varvar_base import create_varvar
from .champ_class_create_bace.pal.pallad import create_pal_base
from .champ_class_create_bace.dru.dru_base import create_dru_base


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
        prist = create_cleric()
        rogue = create_rogue()
        sorcerer = create_sorcerer()
        artif = create_artif()
        kold = create_kold_base()
        pal=create_pal_base()
        dru=create_dru_base()
