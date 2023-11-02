from django.urls import path
from tournament import views

urlpatterns = [
    # Other URL patterns
    path('', views.match_list, name='match-list'),
]
