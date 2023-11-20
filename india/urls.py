from india.views import *
from django.urls import path
app_name='india'

urlpatterns=[

path('kohli/',kohli,name='kohli'),
path('iyer/',iyer,name='iyer'),

]