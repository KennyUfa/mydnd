from django.apps import apps
from django.contrib import admin

from dnd.models import *





models = apps.get_models()


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
