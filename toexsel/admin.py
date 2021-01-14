from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Graguate1996)
class Graguate1996Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','usp','pos')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate1997)
class Graguate1997Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','usp')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate1998)
class Graguate1998Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','usp')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate1999)
class Graguate1999Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mak','diplombk','mamangikship','formedu')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate2000)
class Graguate2000Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','hattama','berilgen_kun','usp')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate2001)
class Graguate2001Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','berilgen_kun','usp')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate2002)
class Graguate2002Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','hattama','berilgen_kun','usp')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate2003)
class Graguate2003Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','btrgen_kun','berilgen_kun','mamangikship','usp','srok')
    search_fields = ['diplom_number','fio']

@admin.register(Graguate2004)
class GraguateAdmin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','btrgen_uakyt','berilgen_kun','mamangik','pos')
    search_fields = ['diplom_number','fio']


@admin.register(Graduate2005)
class Graduate2005Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','berilu_merzim','mkk','mamangik','berilgen_kva','pos')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2006)
class Graduate2006Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','duplicate','year')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2007)
class Graduate2007Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','akt','uzd','duplicate','year','ajb')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2008)
class Graduate2008Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','eskertu','address','workplace','fio2','naima')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2009)
class Graduate2009Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','eskertu','address','workplace','fio2')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2010)
class Graduate2010Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','eskertu','reddiplom')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2011)
class Graduate2011Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2012)
class Graduate2012Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','fio','mamangikship','group','birthday','birthyear1','birthyear2','jekekualik','jsn','ctn','nation','azamattik','address','workplace')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2013)
class Graduate2013Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','mak','diplombk','mamangikship','formedu','fio','birthday','pol','nation','dateto')
    search_fields = ['diplom_number','fio']



@admin.register(Graduate2014)
class Graduate2014Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','mak','diplombk','mamangikship','formedu','fio')
    search_fields = ['diplom_number','fio']


@admin.register(Graduate2015)
class Graduate2015Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','mak','diplombk','mamangikship','formedu','fio')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2016)
class Graduate2016Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','mak','diplombk','mamangikship','formedu','fio')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2017)
class Graduate2017Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','mak','diplombk','mamangikship','formedu','fio')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2018)
class Graduate2018Admin(ImportExportModelAdmin):
    list_display = ('id','diplom_number','tirkeu_katar','mak','diplombk','mamangikship','formedu','fio')
    search_fields = ['diplom_number','fio']

@admin.register(Graduate2019och)
class Graduate2019ochAdmin(ImportExportModelAdmin):
    list_display = ('id','surname','name','last_name','diplom_number','untitled','mamangikship','diplombk')
    search_fields = ['diplom_number','name']

@admin.register(Graduate2019zaoch)
class Graduate2019zaochAdmin(ImportExportModelAdmin):
    list_display = ('id','surname','name','last_name','diplom_number','untitled','mamangikship','diplombk')
    search_fields = ['diplom_number','name']








