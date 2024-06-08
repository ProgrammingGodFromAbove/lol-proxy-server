from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings


region = "asia"
api_key = "RGAPI-6307251d-e270-42df-bd59-b6999b68fe4c"
# api_key = settings.RIOT_API_KEY

def get_match_history(request):
    puuid = request.GET.get('puuid')
    if not puuid:
        return JsonResponse({'error': 'PUUID is required'}, status=400)
    
    
    region = "asia"
    start = request.GET.get('start', 0)
    count = request.GET.get('count', 25)

    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={api_key}'
    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from Riot Games API'}, status=response.status_code)
    
    match_ids = response.json()
    return JsonResponse(match_ids, safe=False)

def get_account_by_riot_id(request):
    game_name = request.GET.get('game_name')
    tag_line = request.GET.get('tag_line')
    
    if not game_name or not tag_line:
        return JsonResponse({'error': 'game_name and tag_line are required'}, status=400)
    
  
    region = "asia"

   
    url = f'https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}'
    
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from Riot Games API'}, status=response.status_code)
    
    account_info = response.json()
    print(account_info)
    return JsonResponse(account_info)

def get_match_details(request):
    match_id = request.GET.get('match_id')
    
    if not match_id:
        return JsonResponse({'error': 'match_id is required'}, status=400)
    

    region = "asia"

    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
    
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from Riot Games API'}, status=response.status_code)
    
    match_details = response.json()
    return JsonResponse(match_details)



