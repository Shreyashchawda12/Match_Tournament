from django.urls import path
from tournament import views
from .views import TeamDetailView

urlpatterns = [
    # Other URL patterns
    path('create_match/', views.create_match, name='create-match'),
    path('create_team_match/', views.create_team_match, name='create_team_match'),
    path('team/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('team-summary/', views.TeamSummaryListView.as_view(), name='team-summary'),
   

]
