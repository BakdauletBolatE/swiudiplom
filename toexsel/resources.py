from import_export import resources
from .models import Graguate2004,Graduate2005,Graduate2006,Graduate2007,Graduate2008,Graduate2009,Graduate2010

class GraguateResoureses(resources.ModelResource):
    class Meta:
        model = Graguate2004

class Graduate2005Resources(resources.ModelResource):
    class Meta:
        model = Graduate2005

class Graduate2006Resources(resources.ModelResource):
    class Meta:
        model = Graduate2006

class Graduate2007Resources(resources.ModelResource):
    class Meta:
        model = Graduate2007

class Graduate2008Resources(resources.ModelResource):
    class Meta:
        model = Graduate2008

class Graduate2009Resources(resources.ModelResource):
    class Meta:
        model = Graduate2009

class Graduate2010Resources(resources.ModelResource):
    class Meta:
        model = Graduate2010
        