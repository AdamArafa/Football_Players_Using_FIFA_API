# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:57:24 2021

@author: arafa
"""

import requests 
import time
import pandas as pd

#response = requests.get('https://www.easports.com/fifa/ultimate-team/api/fut/item').json()
#response['items'][0]
#response['totalPages']

base_url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item'

# get the response from the api (by page)

def main_request(base_url, page_num):
    response = requests.get(base_url + '?page={}'.format(page_num)).json()
    return response



# get the total number of pages form request response

def get_total_pages_num(response):
    num_of_pages = response['totalPages']
    return num_of_pages

# get wanted info for each player

def get_needed_info(response):
    players = []
    for player in response['items']:
        player_info = {
             'commonName': player['commonName'],
             'firstName':  player['firstName'],
             'lastName': player['lastName'],
             'country': player['nation']['name'],
             'club': player['club']['name'],
             'position': player['position'],
             'composure': player['composure'],
             'playStyle': player['playStyle'],
             'playStyleId': player['playStyleId'],
             'height': player['height'],
             'weight': player['weight'],
             'birthday': player['birthdate'],
             'age': player['age'],
             'acceleration': player['acceleration'],
             'aggression': player['aggression'],
             'agility': player['agility'],
             'balance': player['balance'],
             'ballcontrol': player['ballcontrol'],
             'foot': player['foot'],
             'skillMoves': player['skillMoves'],
             'crossing': player['crossing'],
             'curve': player['curve'],
             'dribbling': player['dribbling'],
             'finishing': player['finishing'],
             'freekickaccuracy': player['freekickaccuracy'],
             'gkdiving': player['gkdiving'],
             'gkhandling': player['gkhandling'],
             'gkkicking': player['gkkicking'],
             'gkpositioning': player['gkpositioning'],
             'gkreflexes': player['gkreflexes'],
             'headingaccuracy': player['headingaccuracy'],
             'interceptions': player['interceptions'],
             'jumping': player['jumping'],
             'longpassing': player['longpassing'],
             'longshots': player['longshots'],
             'marking': player['marking'],
             'penalties': player['penalties'],
             'positioning': player['positioning'],
             'potential': player['potential'],
             'reactions': player['reactions'],
             'shortpassing': player['shortpassing'],
             'shotpower': player['shotpower'],
             'slidingtackle': player['slidingtackle'],
             'sprintspeed': player['sprintspeed'],
             'standingtackle': player['standingtackle'],
             'stamina': player['stamina'],
             'strength': player['strength'],
             'vision': player['vision'],
             'volleys': player['volleys'],
             'weakFoot': player['weakFoot'],
             'quality': player['quality'],
             'isLoan': player['isLoan'],
             'rating': player['rating']
             
        }
        
        
        players.append(player_info)
        
    return players

all_data = []

data = main_request(base_url, 1)
for p in range(1, get_total_pages_num(data)+1):
    print(p)
    r = main_request(base_url, p)
    all_data.extend(get_needed_info(r))
    
df = pd.DataFrame(all_data)

print(df.shape[0])

df.to_csv('players_data.csv', index = False)
    

        
        
        
        
        
        
    

#response['items'][0]['quality']

#for player in response['items']:
#        player_commonName = player['commonName']
#        player_firstName = player['firstName']
#        player_lastName = player['lastName']
#        
#        print(player_commonName)
#        print(player_firstName)
#        print(player_lastName)