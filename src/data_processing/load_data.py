from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

# Specify the season (2023)
season = '2023'  # Try for the previous season

# Create the endpoint object for player stats (no team_id parameter)
player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season=season)

# Inspect the raw data returned by the API
data = player_stats.get_data()

# Print the raw data to inspect it
print(data)

# Check if the data is valid and has the correct structure
if "data" in data:
    # Convert the response data to a pandas DataFrame
    df = pd.DataFrame(data["data"], columns=data["headers"])
    
    # Filter the data to include only players from the New York Knicks (team_id for the Knicks is 1)
    df_knicks = df[df['team_id'] == 1]  # Team ID for the New York Knicks is 1

    # Clean column names (convert them to lowercase)
    df_knicks.columns = df_knicks.columns.str.lower()

    # Save the cleaned data as a CSV file
    df_knicks.to_csv('data/raw/knicks_player_stats_api_2023.csv', index=False)

    print("Data fetched and saved successfully.")
else:
    print("Error: Data structure is not as expected.")


