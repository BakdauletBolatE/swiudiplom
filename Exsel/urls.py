from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.http import  HttpResponse
# from newdiplom.models import SwiuDiplom2020

# def deleteAll(request):
#     SwiuDiplom2020.objects.all().delete()
#     return HttpResponse('Succes')


urlpatterns = [
    # path('delete/',deleteAll),
    path('', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

