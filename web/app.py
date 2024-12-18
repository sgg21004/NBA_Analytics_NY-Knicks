# web/app.py

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)

def create_performance_chart(player_name, data):
    player_data = data[data['PLAYER'] == player_name]
    points = player_data['PTS'].mean()
    assists = player_data['AST'].mean()
    rebounds = player_data['REB'].mean()
    fg_percentage = player_data['FG%'].mean()

    metrics = ['Points', 'Assists', 'Rebounds', 'Field Goal Percentage']
    values = [points, assists, rebounds, fg_percentage]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=metrics, y=values, palette='Blues', ax=ax)
    ax.set_title(f"Performance Analysis for {player_name}")

    # Convert chart to base64 for embedding in HTML
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode('utf-8')

    return chart_url

@app.route('/')
def home():
    # Load the cleaned data
    clean_data = pd.read_csv("data/processed/knicks_cleaned_stats.csv")

    # Default player for analysis
    player_name = "Jalen Brunson"

    # Generate performance chart
    chart_url = create_performance_chart(player_name, clean_data)

    return render_template('index.html', player_name=player_name, chart_url=chart_url)

if __name__ == "__main__":
    app.run(debug=True)
