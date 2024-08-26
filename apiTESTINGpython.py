import requests
import pandas as pd

r = requests.get('https://api-web.nhle.com/v1/player/8478402/landing')

data = r.json()

first_name = data['firstName']['default']
last_name = data['lastName']['default']
birth_country = data['birthCountry']
player_ID = data['playerId']
position = data['position']
draft_year = data['draftDetails']['year']
games_played = data['careerTotals']['regularSeason']['gamesPlayed']
goals = data['careerTotals']['regularSeason']['goals']
assists = data['careerTotals']['regularSeason']['assists']
points = data['careerTotals']['regularSeason']['points']

df = pd.DataFrame({
    'playerID': [player_ID],
    'firstName': [first_name],
    'lastName': [last_name],
    'birth_country': [birth_country],
    'position': [position],
    'draftYear': [draft_year],
    'GamesPlayed': [games_played],
    'Goals': [goals],
    'Assists': [assists],
    'Points': [points]
})

print(df)