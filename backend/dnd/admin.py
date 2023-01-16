from django.contrib import admin
# from .models import *
from django.apps import apps
# link,name,lvl,school,Время накладывания,Дистанция,Компоненты,Длительность,Классы,Архетипы,Источник,Описание


class DndAdmin(admin.ModelAdmin):
    list_display = ("name", "lvl")
    list_display_links = ("name", "lvl")
    search_fields = ("name", "lvl")


# admin.site.register(DndSpell, DndAdmin)
# admin.site.register(Character)
# admin.site.register(BaseClassCh)
# # admin.site.register(PreHistory)
# admin.site.register(Race)
# admin.site.register(WorldOutlook)
# admin.site.register(PreHistoryModel)

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
