from django.urls import path
from minhas_pages.views import home, screenOne, screenTwo, screenThree

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('home/pageOne/', screenOne, name='pageOne'),
    path('home/pageTwo/', screenTwo, name='pageTwo'),
    path('home/pageThree/', screenThree, name='pageThree'),
]