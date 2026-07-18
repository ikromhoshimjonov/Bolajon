from django.contrib import admin
from django.contrib.auth.models import Group


from apps.models import Bolajon


@admin.register(Bolajon)
class HomeAdmin(admin.ModelAdmin):
    pass
