from django.urls import path
from minhas_pages.views import home, screenOne, screenTwo

urlpatterns = [
    path('home/', home),
    path('home/pageOne/', screenOne),
    path('home/pageTwo/', screenTwo),
]