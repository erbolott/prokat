
from django.urls import path
from .views import Home, search ,news , contact_page , uslovia_page, tablitsa_razmerov

urlpatterns = [
    path('' , Home , name='home'),
    path('search/',search, name="search"),
    path('news/',news , name="news"),
    path('contact/' , contact_page , name='contact'),
    path('uslovia/', uslovia_page , name='uslovia'),
    path('tablitsa-razmerov/', tablitsa_razmerov , name='tablitsa_razmerov'),
]