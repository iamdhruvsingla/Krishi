from flask import Flask, render_template
import requests

app = Flask(__name__)

# Your Visual Crossing API key
WEATHER_API_KEY = 'RTDVH3CMK8Q3D7XM7NTYBPDBH'
WEATHER_API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'

def get_weather_data():
    # Example location, replace with actual location or user input
    location = 'Rohtak'
    response = requests.get(f'{WEATHER_API_URL}/{location}', params={'key': WEATHER_API_KEY})
    return response.json()

@app.route('/')
def index():
    weather_data = get_weather_data()
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
