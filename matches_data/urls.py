from django.urls import path
from . import views

urlpatterns = [
    # Main endpoints
    path('matches', views.get_matches, name='get_matches'),
    path('matches/sport', views.get_matches_by_sport, name='get_matches_by_sport'),
    path('matches/sport/country', views.get_matches_by_sport_country, name='get_matches_by_sport_country'),
    path('matches/date-range', views.get_matches_by_date_range, name='get_matches_by_date_range'),
    path('matches/with-odds', views.get_matches_with_odds, name='get_matches_with_odds'),
    path('match/<str:match_id>', views.get_match_by_id, name='get_match_by_id'),

    # Sports and metadata
    path('sports', views.get_all_sports, name='get_all_sports'),
    path('countries', views.get_countries, name='get_all_countries'),
    path('games', views.get_matches_by_sport_country_games, name='get_matches_by_sport_country_games'),
    path('live_games', views.get_live_matches, name='get_live_matches'),
    path('match_by_id', views.get_match_by_id_, name='get_match_by_id'),
    path('matches_data_check', views.matches_data_check, name='matches_data_check'),
]