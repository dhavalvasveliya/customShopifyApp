from flask import Flask, request, jsonify, render_template
import googlemaps
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()

@app.route('/ratings', methods=['GET'])
def respond():
    
    gmaps = googlemaps.Client(key=os.getenv("GOOGLE_API_KEY"))

    place = gmaps.place('ChIJDRGiQA39zUwRHzX2ExFiRG0')
    ratings = place['result']['rating']
    total_ratings = place['result']['user_ratings_total']

    return render_template('ratings.html', ratings=ratings, total_ratings=total_ratings)




@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>WowMat Store API</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)