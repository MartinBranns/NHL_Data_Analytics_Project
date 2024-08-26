import requests
import pandas as pd

start_id = 8478000
end_id = 8479000

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
                
                # Check if required keys are present
                if 'firstName' in player_data and 'lastName' in player_data and 'birthCountry' in player_data:
                    first_name = player_data['firstName']['default']
                    last_name = player_data['lastName']['default']
                    birth_country = player_data['birthCountry']

                    players_list.append({
                        'firstName': first_name,
                        'lastName': last_name,
                        'birthCountry': birth_country
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
df.to_csv('nhl_players2.csv', index=False)

# Print DataFrame
print(df)
print("Data saved to nhl_players.csv")