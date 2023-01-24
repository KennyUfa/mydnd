from django.contrib import admin
from django.apps import apps


class DndAdmin(admin.ModelAdmin):
    list_display = ("name", "lvl")
    list_display_links = ("name", "lvl")
    search_fields = ("name", "lvl")



models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
