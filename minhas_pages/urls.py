from django.urls import path
from minhas_pages.views import home, screenOne, screenTwo

urlpatterns = [
    path('home/', home, name='home'),
    path('home/pageOne/', screenOne, name='pageOne'),
    path('home/pageTwo/', screenTwo, name='pageTwo'),
]