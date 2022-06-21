from importlib.resources import path
from flask import Flask, request, jsonify, render_template, send_from_directory
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

    rating_response = {'rating':ratings,'totalratings':total_ratings}

    return render_template('ratings.html')

@app.route('/staic/app.js')
def jsfile():
    return send_from_directory('app.js','static/app.js')

@app.route('/staic/app.css')
def cssfile():
    return send_from_directory('app.css','static/app.css')


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>WowMat Store API</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)