from django.test import TestCase
from .models import SwiuDiplom2020
# Create your tests here.
def delete_everything(self):
    SwiuDiplom2020.objects.all().delete()

