from django.contrib import admin
from django.urls import path
from toexsel.views import home,Graduate2004List,Graduate2005List,Graduate2006List,Graduate2007List,Graduate2008List,Graduate2009List,Graduate2010List

urlpatterns = [
    path('',home,name="home"),
    path('2004/',Graduate2004List.as_view(),name="graduate2004list"),
    path('2005/',Graduate2005List.as_view(),name="graduate2005list"),
    path('2006/',Graduate2006List.as_view(),name="graduate2006list"),
    path('2007/',Graduate2007List.as_view(),name="graduate2007list"),
    path('2008/',Graduate2008List.as_view(),name="graduate2008list"),
    path('2009/',Graduate2009List.as_view(),name="graduate2009list"),
    path('2010/',Graduate2010List.as_view(),name="graduate2010list")
]