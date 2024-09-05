# app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = 'vb9qi0LClA3ZVpBeOGVE94Pd2G0xa8iB4fJp6Wta'
ENDPOINT = 'https://open-api.bser.io'
API_PATH = '/v1/user/nickname'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.json.get('query')
    
    if not user_query:
        return jsonify({'error': 'Query is required'}), 400

    # Headers for the API request
    headers = {
        'accept': 'application/json',
        'x-api-key': API_KEY
    }

    # Parameters with user input
    params = {
        'query': user_query,
    }

    try:
        # Make the request
        r = requests.get(ENDPOINT + API_PATH, headers=headers, params=params)

        # Check if the response contains valid JSON
        r.raise_for_status()  # Raise an HTTPError for bad responses
        data = r.json()

    except requests.exceptions.RequestException as e:
        # In case of any exception, return a message with status code 500
        return jsonify({'error': 'Failed to fetch data', 'details': str(e)}), 500

    # Return the JSON response back to the frontend
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
