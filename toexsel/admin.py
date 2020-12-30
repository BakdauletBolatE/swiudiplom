from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Graguate2004,Graduate2005,Graduate2006,Graduate2007,Graduate2008,Graduate2009,Graduate2010

# Register your models here.
@admin.register(Graguate2004)
class GraguateAdmin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','btrgen_uakyt','berilgen_kun','mamangik','pos')



@admin.register(Graduate2005)
class Graduate2005Admin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','berilu_merzim','mkk','mamangik','berilgen_kva','pos')

@admin.register(Graduate2006)
class Graduate2006Admin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','mamangikship','duplicate','year')

@admin.register(Graduate2007)
class Graduate2007Admin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','mamangikship','akt','uzd','duplicate','year','ajb')

@admin.register(Graduate2008)
class Graduate2008Admin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','mamangikship','eskertu','address','workplace','fio2','naima')

@admin.register(Graduate2009)
class Graduate2009Admin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','mamangikship','eskertu','address','workplace','fio2')

@admin.register(Graduate2010)
class Graduate2010Admin(ImportExportModelAdmin):
    list_display = ('diplom_number','tirkeu_katar','fio','mamangikship','eskertu','reddiplom')

