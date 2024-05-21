from django.urls import path
from .views import *



urlpatterns = [


    path('account-by-riot-id/', get_account_by_riot_id, name='get_account_by_riot_id'),
    path('match-history/', get_match_history, name='get_match_history'),
    path('match-details/', get_match_details, name='get_match_details'),
]
