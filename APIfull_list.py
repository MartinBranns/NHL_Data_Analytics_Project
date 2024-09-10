import requests
import pandas as pd

start_id = 8478000
end_id = 8479200

# Generate a list of player IDs
player_ids = [str(id) for id in range(start_id, end_id + 1)]
players_list = []

for player_id in player_ids:
    try:
        # Fetch player data
        player_response = requests.get(f'https://api-web.nhle.com/v1/player/{player_id}/landing')
        
        # Check if the request was successful
        if player_response.status_code == 200:
            try:
                # Attempt to parse JSON
                player_data = player_response.json()
                
                           # Use get() method to safely access dictionary keys
                first_name = player_data.get('firstName', {}).get('default', 'N/A')
                last_name = player_data.get('lastName', {}).get('default', 'N/A')
                birth_country = player_data.get('birthCountry', 'N/A')
                player_ID = player_data.get('playerId', 'N/A')
                position = player_data.get('position', 'N/A')
                
                draft_details = player_data.get('draftDetails', {})
                draft_year = draft_details.get('year', 'N/A')
                
                career_totals = player_data.get('careerTotals', {}).get('regularSeason', {})
                games_played = career_totals.get('gamesPlayed', 'N/A')
                goals = career_totals.get('goals', 'N/A')
                assists = career_totals.get('assists', 'N/A')
                points = career_totals.get('points', 'N/A')

                players_list.append({
                    'playerID': player_ID,
                    'firstName': first_name,
                    'lastName': last_name,
                    'birth_country': birth_country,
                    'position': position,
                    'draftYear': draft_year,
                    'GamesPlayed': games_played,
                    'Goals': goals,
                    'Assists': assists,
                    'Points': points
                    })
            except ValueError:
                print(f"Error decoding JSON for player ID {player_id}: {player_response.text}")
        else:
            print(f"Failed request for player ID {player_id}: Status code {player_response.status_code}")
    
    except requests.RequestException as e:
        print(f"Request exception for player ID {player_id}: {e}")

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(players_list)

# Save the DataFrame to a CSV file
df.to_csv('nhl_players_5.csv', index=False)

# Print DataFrame
print(df)
print("Data saved to nhl_players_5.csv")
