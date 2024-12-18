# src/dashboard/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.analysis.player_performance_analysis import plot_performance, compare_players
from src.visualizations.shot_simulation_visualization import plot_shot_simulation

def main():
    st.title("NBA Player Analytics Dashboard")
    
    # Load the cleaned data
    clean_data = pd.read_csv("data/processed/knicks_cleaned_stats.csv")
    
    # Sidebar for selecting a player
    player_names = clean_data['PLAYER'].unique()
    player_name = st.sidebar.selectbox("Select a player", player_names)
    
    st.subheader(f"Performance Analysis for {player_name}")
    plot_performance(player_name, clean_data)
    
    # Show shot simulation results
    if st.sidebar.checkbox('Show Shot Simulation'):
        st.subheader(f"Shot Simulation for {player_name}")
        plot_shot_simulation(player_name, clean_data)
    
    # Player comparison
    st.subheader("Compare Player Performance")
    comparison_players = st.sidebar.multiselect("Select players to compare", player_names, default=["Jalen Brunson", "Julius Randle"])
    if len(comparison_players) > 1:
        compare_players(comparison_players, clean_data)

if __name__ == "__main__":
    main()
