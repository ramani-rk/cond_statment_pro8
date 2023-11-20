from app.views import *
from django.urls import path
app_name = 'conditions'

urlpatterns = [
    path('ifstatement/',ifstatement, name = 'ifstatement'),
    path('ifelse/',ifelse, name = 'ifelse'),
    path('ifelif/',ifelif, name = 'ifelif'),
    path('nested/',nested, name = 'nested'),

]