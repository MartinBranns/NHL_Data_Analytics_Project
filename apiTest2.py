import requests
import pandas as pd

start_id = 8478395
end_id = 8478500

# Generate a list of player IDs
player_ids = [str(id) for id in range(start_id, end_id + 1)]
players_list = []

for player_id in player_ids:
    player_response = requests.get(f'https://api-web.nhle.com/v1/player/{player_id}/landing')
    player_data = player_response.json()

    if 'firstName' in player_data and 'lastName' in player_data and 'birthCountry' in player_data:
        first_name = player_data['firstName']['default']
        last_name = player_data['lastName']['default']
        birth_country = player_data['birthCountry']

        players_list.append({
            'firstName': first_name,
            'lastName': last_name,
            'birth_country': birth_country})
    else:
        pass
     

df = pd.DataFrame(players_list)

print(df)
