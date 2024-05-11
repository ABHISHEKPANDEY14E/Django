from django.urls import path
from . import views
from .views import index
    
urlpatterns = [
    path("", views.index, name="index"),  # /challenges/
    path('challenges/', index, name='challenges-index'),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
