from django.contrib import admin
from django.apps import apps

allModels = apps.get_app_config('application').get_models()

# Register your models here.
for model in allModels:
    admin.site.register(model)