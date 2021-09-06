from django.contrib import admin
from django.forms import models

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ReportDate,FoundItems

class FoundItemsResource(resources.ModelResource):
    class Meta:
        model = FoundItems

@admin.register(FoundItems)
class FoundItemsAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display = ('hotels','FoundItems_Year','FoundItems_Month','files','create_user','create_date')
    form_encording = 'utf-8'

    resource_class = FoundItemsResource

admin.site.register(ReportDate)