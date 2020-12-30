from django.shortcuts import render
from .models import Graguate2004,Graduate2005,Graduate2006,Graduate2007,Graduate2008,Graduate2009,Graduate2010
from .resources import GraguateResoureses
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.views.generic import ListView

def home(request):
    return render(request,'toexsel/home.html')
class Graduate2004List(ListView):
    paginate_by = 20
    model = Graguate2004

class Graduate2005List(ListView):
    paginate_by = 20
    model = Graduate2005

class Graduate2006List(ListView):
    paginate_by = 20
    model = Graduate2006

class Graduate2007List(ListView):
    paginate_by = 20
    model = Graduate2007

class Graduate2008List(ListView):
    paginate_by = 20
    model = Graduate2008

class Graduate2009List(ListView):
    paginate_by = 20
    model = Graduate2009

class Graduate2010List(ListView):
    paginate_by = 20
    model = Graduate2010




# Create your views here.

# def simple_upload(request):
#     if request.method == "POST":
#         graduate_resoures = GraguateResoureses()
#         dataset = Dataset()
#         new_graduate = request.FILES['file']
#         if not new_graduate.name.endswith('xlsx'):
#             messages.info(request,"wrong format")
#             return render(request,'upload.html')
#         imported_data = dataset.load(new_graduate.read(),format="xlsx")
#         for data in imported_data:
#             value = Graguate(
#                 data[0],
#                 data[1],
#                 data[2],
#                 data[3],
#                 data[4],
#                 data[5],
#                 data[6],
#             )
#             value.save()
#         return render(request,'upload.html')
#     return render(request,'upload.html')


