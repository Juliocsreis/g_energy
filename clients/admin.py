from django.contrib import admin
from .models import Client
from import_export.admin import ImportExportModelAdmin


class ClientImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'email', ]
    pass


admin.site.register(Client, ClientImportExport)