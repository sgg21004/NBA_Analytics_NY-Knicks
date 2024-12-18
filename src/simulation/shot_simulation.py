# src/simulation/shot_simulation.py

import random
import pandas as pd

def simulate_shots(player_name, data, num_shots=100):
    # Filter data for the selected player
    player_data = data[data['PLAYER'] == player_name]
    
    # Assuming 'FG%' (field goal percentage) is in the data, or you can use another column for shot efficiency
    fg_percentage = player_data['FG%'].mean()  # Field Goal Percentage for the player

    print(f"Simulating {num_shots} shots for {player_name} with {fg_percentage*100:.2f}% FG%")

    # Simulate shots
    made_shots = 0
    missed_shots = 0

    for _ in range(num_shots):
        shot_outcome = random.random() < fg_percentage  # Simulate shot outcome (True for made, False for missed)
        if shot_outcome:
            made_shots += 1
        else:
            missed_shots += 1

    # Display the result
    print(f"Made Shots: {made_shots}")
    print(f"Missed Shots: {missed_shots}")
    print(f"Shot Accuracy: {made_shots / num_shots * 100:.2f}%")

if __name__ == "__main__":
    # Load the cleaned data
    clean_data = pd.read_csv("data/processed/knicks_cleaned_stats.csv")
    
    # Simulate shots for a player (e.g., Jalen Brunson)
    simulate_shots("Jalen Brunson", clean_data)
