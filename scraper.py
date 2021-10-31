# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:52:42 2021

@author: arafa
"""

import selenium
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver as wb
from tqdm import tqdm
import pandas as pd

# open the website

webD = wb.Chrome('chromedriver.exe')
url = 'https://sofifa.com/players?r=210064&set=true'
webD.get(url)

# to accept all the cookies you have to switch to a different frame and then find the xpath to the accept all button

# switch/move this frame
#webD.switch_to_frame('gdpr-consent-notice')

# accept all cookies
#webD.find_element_by_xpath('//*[@id="save"]/span[1]/div').click()

players_urls = []
condition = True

while condition:
    players_lst = webD.find_element_by_class_name('list').find_elements_by_tag_name('tr')
    for p in players_lst:
        try:
            player_url = p.find_element_by_class_name('tooltip').get_property('href')
            players_urls.append(player_url)
        except:
            continue
    try:
        next_btn = webD.find_element_by_xpath('//*[@id="adjust"]/div/div[1]/div/div/a[2]/span[1]')
        next_btn.click()
    except:
        try:
            next_btn1 =  webD.find_element_by_xpath('//*[@id="adjust"]/div/div[1]/div/div/a/span[1]')
            next_btn1.click()
        except:
            condition=False
                
                    
# what I want to collect for each player

# for testing 

'''
player_info = {
    'name': webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/div/h1').text,
    'country': webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/div/div/a').get_property('title'),
    'personal_info': webD.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div/div').text,
    'overall_Rating': webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/section/div[1]/div/span').text,
    'potential': webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/section/div[2]/div/span').text,
    'value': webD.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/section/div[3]/div').text,
    'wage': webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/section/div[4]/div').text,
    'preferred_foot':webD.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/div/ul/li[1]').text,
    'weak_foot':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[2]').text,
    'skill_moves':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[3]').text,
    'international_reputation':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[4]').text,
    'work_rate':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[5]/span').text,
    'body_type':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[6]/span').text,
    'release_clause':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[8]/span').text,
    'id':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[9]').text,
    'player_specialities':[el.text for el in webD.find_elements_by_xpath("//*[@id='list']/div[2]/div/div/div/div[1]/div[3]/div/ul")],
    'current_club':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/h5/a').text,
    'club_country':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/h5/a/img').get_property('title'),
    'position':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[2]/span').text,
    'jersey_number':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[3]').text,
    'joined_club':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[4]').text,
    'contract_valid_until':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[5]').text[-4:],
    'crossing':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[1]/span[1]').text,
    'finishing':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[2]/span[1]').text,
    'heading_accuracy':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[3]/span[1]').text,
    'short_passing':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[4]/span[1]').text,
    'volleys':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[5]/span[1]').text,
    'dribbling':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[1]/span[1]').text,
    'curve':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[2]/span[1]').text,
    'fk_accuracy':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[3]/span[1]').text,
    'long_passing':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[4]/span[1]').text,
    'ball_control':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[5]/span[1]').text,
    'acceleration':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[1]/span[1]').text,
    'sprint_speed':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[2]/span[1]').text,
    'agility':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[3]/span[1]').text,
    'reactions':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[4]/span[1]').text,
    'balance':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[5]/span[1]').text,
    'shot_power':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[1]/span[1]').text,
    'jumping':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[2]/span[1]').text,
    'stamina':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[3]/span[1]').text,
    'strength':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[4]/span[1]').text,
    'long_shots':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[5]/span[1]').text,
    'aggression':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[1]/span[1]').text,
    'interceptions':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[2]/span[1]').text,
    'positioning':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[3]/span[1]').text,
    'vision':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[4]/span[1]').text,
    'penalties':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[5]/span[1]').text,
    'composure':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[6]/span').text,
    'defensive_awareness':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[1]/span[1]').text,
    'standing_tackle':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[2]/span[1]').text,
    'sliding_tackle':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[3]/span[1]').text,
    'gk_diving':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[3]/span[1]').text,
    'gk_handling':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[2]/span').text,
    'gk_kicking':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[3]/span').text,
    'gk_positioning':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[4]/span').text,
    'gk_reflexes':webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[5]/span').text,

    }

player_info

'''
    
#len(set(players_urls))
#len(all_removed_players_urls)

# what I want to collect for each player

all_players_info = []

all_removed_players_urls = []

# I got this exception (TimeoutException: timeout: Timed out receiving message from renderer: 299.656
# (Session info: chrome=95.0.4638.54)) while running the code to collect every player data. 
# To overcome this problem I will do that:
# run the for loop --> collect a player data --> remove the player url from 
# 'players_urls list' and save it to another temp list (just incase) --> when the code stop again, 
# just run the for loop on the rest of the players urls

# original for loop was: for i in tqdm(set(players_urls)):
    
for i in tqdm(set(players_urls[:])):
    
    webD.get(i)
    
    try:
        name =  webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/div/h1').text
    except NoSuchElementException:
        name = 'empty'
    try:
        country =  webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/div/div/a').get_property('title')
    except:
        country = 'empty'
    try:
        personal_info = webD.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/div/div').text
    except:
        personal_info = 'empty'
    try:
        overall_rating = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/section/div[1]/div/span').text
    except:
        overall_rating = 'empty'
    try:
        potential = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/section/div[2]/div/span').text
    except:
        potential = 'empty'
    try:
        value = webD.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[1]/section/div[3]/div').text
    except:
        value = 'empty'
    try:
        wage = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[1]/section/div[4]/div').text
    except:
        wage = 'empty'
    try:
        preferred_foot = webD.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/div/ul/li[1]').text
    except:
        preferred_foot = 'empty'
    try:
        weak_foot = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[2]').text
    except:
        weak_foot = 'empty'
    try:  
        skill_moves = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[3]').text
    except:
        skill_moves = 'empty'
    try:
        international_reputation = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[4]').text
    except:
        international_reputation = 'empty'
    try:
        work_rate = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[5]/span').text
    except:
        work_rate = 'empty'
    try:
        body_type = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[6]/span').text
    except:
        body_type = 'empty'
    try:
        release_clause = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[8]/span').text
    except:
        release_clause = 'empty'
    try:
        Id = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[9]').text
    except:
        Id = 'empty'
    try:
        all_spec = [el.text for el in webD.find_elements_by_xpath("//*[@id='list']/div[2]/div/div/div/div[1]/div[3]/div/ul")]
        player_specialities = ' '.join(all_spec)
    except:
        player_specialities = 'empty'
    try:
        current_club = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/h5/a').text
    except:
        current_club = 'empty'
    try:
        club_country = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/h5/a/img').get_property('title')
    except:
        club_country = 'empty'
    try:
        position = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[2]/span').text
    except:
        position = 'empty'
    try:
        jersey_number = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[3]').text
    except:
        jersey_number = 'empty'
    try:
        joined_club = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[4]').text
    except:
        joined_club = 'empty'
    try:
        contract_valid_until = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[4]/div/ul/li[5]').text[-4:]
    except:
        contract_valid_until = 'empty'
    try:
        crossing = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[1]/span[1]').text
    except:
        crossing = 'empty'
    try:
        finishing = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[2]/span[1]').text
    except:
        finishing = 'empty'
    try:
        heading_accuracy = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[3]/span[1]').text
    except:
        heading_accuracy = 'empty'
    try:
        short_passing = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[4]/span[1]').text
    except:
        short_passing = 'empty'
    try:
        volleys = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[8]/div/ul/li[5]/span[1]').text
    except:
        volleys = 'empty'
    try:
        dribbling = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[1]/span[1]').text
    except:
        dribbling = 'empty'
    try:
        curve = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[2]/span[1]').text
    except:
        curve = 'empty'
    try:
        fk_accuracy = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[3]/span[1]').text
    except:
        fk_accuracy = 'empty'
    try:
        long_passing = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[4]/span[1]').text
    except:
        long_passing = 'empty'
    try:
        ball_control = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[9]/div/ul/li[5]/span[1]').text
    except:
        ball_control = 'empty'
    try:
        acceleration = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[1]/span[1]').text
    except:
        acceleration = 'empty'
    try:
        sprint_speed = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[2]/span[1]').text
    except:
        sprint_speed = 'empty'
    try:
        agility = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[3]/span[1]').text
    except:
        agility = 'empty'
    try:
        reactions = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[4]/span[1]').text
    except:
        reactions = 'empty'
    try:
        balance = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[10]/div/ul/li[5]/span[1]').text
    except:
        balance = 'empty'
    try:
        shot_power = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[1]/span[1]').text
    except:
        shot_power = 'empty'
    try:
        jumping = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[2]/span[1]').text
    except:
        jumping = 'empty'
    try:
        stamina = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[3]/span[1]').text
    except:
        stamina = 'empty'
    try:
        strength = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[4]/span[1]').text
    except:
        strength = 'empty'
    try:
        long_shots = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[11]/div/ul/li[5]/span[1]').text
    except:
        long_shots = 'empty'
    try:
        aggression = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[1]/span[1]').text
    except:
        aggression = 'empty'
    try:
        interceptions = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[2]/span[1]').text
    except:
        interceptions = 'empty'
    try:
        positioning = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[3]/span[1]').text
    except:
        positioning = 'empty'
    try:
        vision = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[4]/span[1]').text
    except:
        vision = 'empty'
    try:
        penalties = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[5]/span[1]').text
    except:
        penalties = 'empty'
    try:
        composure = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[12]/div/ul/li[6]/span').text
    except:
        composure = 'empty'
    try:
        defensive_awareness = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[1]/span[1]').text
    except:
        defensive_awareness = 'empty'
    try:
        standing_tackle = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[2]/span[1]').text
    except:
        standing_tackle = 'empty'
    try:
        sliding_tackle = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[3]/span[1]').text
    except:
        sliding_tackle = 'empty'
    try:
        gk_diving = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[13]/div/ul/li[3]/span[1]').text
    except:
        gk_diving = 'empty'
    try:
        gk_handling = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[2]/span').text
    except:
        gk_handling = 'empty'
    try:
        gk_kicking = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[3]/span').text
    except:
        gk_kicking = 'empty'
    try:
        gk_positioning = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[4]/span').text
    except:
        gk_positioning = 'empty'
    try:
        gk_reflexes = webD.find_element_by_xpath('//*[@id="list"]/div[2]/div/div/div/div[1]/div[14]/div/ul/li[5]/span').text
    except:
        gk_reflexes = 'empty'
        
    a_player_info = {
        'name': name,
        'country': country,
        'personal_info': personal_info,
        'overall_rating': overall_rating,
        'potential': potential,
        'value': value,
        'wage': wage,
        'preferred_foot': preferred_foot,
        'weak_foot': weak_foot,
        'skill_moves': skill_moves,
        'international_reputation':international_reputation,
        'work_rate':work_rate,
        'body_type':body_type,
        'release_clause':release_clause,
        'Id':Id,
        'player_specialities':player_specialities,
        'current_club':current_club,
        'club_country':club_country,
        'position':position,
        'jersey_number':jersey_number,
        'joined_club':joined_club,
        'contract_valid_until':contract_valid_until,
        'crossing':crossing,
        'finishing':finishing,
        'heading_accuracy':heading_accuracy,
        'short_passing':short_passing,
        'volleys':volleys,
        'dribbling':dribbling,
        'curve':curve,
        'fk_accuracy':fk_accuracy,
        'long_passing':long_passing,
        'ball_control':ball_control,
        'acceleration':acceleration,
        'sprint_speed':sprint_speed,
        'agility':agility,
        'reactions':reactions,
        'balance':balance,
        'shot_power':shot_power,
        'jumping':jumping,
        'stamina':stamina,
        'strength':strength,
        'long_shots':long_shots,
        'aggression':aggression,
        'interceptions':interceptions,
        'positioning':positioning,
        'vision':vision,
        'penalties':penalties,
        'composure':composure,
        'defensive_awareness':defensive_awareness,
        'standing_tackle':standing_tackle,
        'sliding_tackle':sliding_tackle,
        'gk_diving':gk_diving,
        'gk_handling':gk_handling,
        'gk_kicking':gk_kicking,
        'gk_positioning':gk_positioning,
        'gk_reflexes':gk_reflexes
        }
    
    all_players_info.append(a_player_info)
    all_removed_players_urls.append(i)
    players_urls.remove(i)

# create pandas dataframe out of the all_players_info list
df = pd.DataFrame(all_players_info)
df.shape

# save the dataframe 
df.to_csv('scraped_fifa21_data.csv', index=False)

# reading the saved data file
read_data = pd.read_csv('scraped_fifa21_data.csv')
read_data.head()



