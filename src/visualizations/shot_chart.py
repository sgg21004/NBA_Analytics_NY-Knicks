# src/visualizations/shot_chart.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_shot_chart(player_name, data):
    # Filter data for the selected player
    player_data = data[data['PLAYER'] == player_name]

    # Example of plotting shot locations (simplified)
    # We assume there are 'SHOT_X' and 'SHOT_Y' columns in the cleaned data for shot locations
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='SHOT_X', y='SHOT_Y', data=player_data, hue='SHOT_MADE', palette='coolwarm', marker='o')

    # Add court outline (simplified version)
    plt.axhline(y=0, color='gray', linewidth=2)
    plt.axvline(x=0, color='gray', linewidth=2)

    plt.title(f'{player_name} Shot Chart')
    plt.xlabel('Court X')
    plt.ylabel('Court Y')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Load cleaned data
    clean_data = pd.read_csv("data/processed/knicks_cleaned_stats.csv")
    
    # Call the function for Jalen Brunson (as an example)
    plot_shot_chart("Jalen Brunson", clean_data)
