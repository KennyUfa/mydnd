from django.apps import apps
from django.contrib import admin

from dnd.models import *





models = apps.get_models()

# class WeaponInline(admin.StackedInline):
#     model = Weapon
#     extra = 0
#
#
# class ShieldInline(admin.StackedInline):
#     model = Shield
#     extra = 0
#
#
# class WeaponAdmin(admin.ModelAdmin):
#     inlines = [WeaponInline, ShieldInline]
#     list_display = ["name", "type"]
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ["name", "type"]
#
# admin.site.register(Item, WeaponAdmin)


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
