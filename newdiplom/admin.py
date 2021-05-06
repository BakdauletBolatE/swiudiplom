from django.contrib import admin
from .models import SwiuDiplomBefore2018,SwiuDiplom2019
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(SwiuDiplomBefore2018)
class SwiuDiplomBefore2018Admin(ImportExportModelAdmin):
    list_display = ('id','fio','dateEnter','degreeAcademic','dateOut','registrationDimplom','formEducation')
    list_filter = ['dateOut','formEducation','nameUniversity']
    search_fields = ['dateEnter','fio']


@admin.register(SwiuDiplom2019)
class SwiuDiplom2019Admin(ImportExportModelAdmin):
    list_display = ('id','lastName','name','dateEnter','degreeAcademic','dateOut','registrationDimplom','formEducation')
    list_filter = ['dateOut','formEducation','nameUniversity']
    search_fields = ['dateEnter','fio']

