from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
import requests
import os
from dotenv import load_dotenv
import traceback
from datetime import datetime, timedelta
import numpy as np
import json
from google.cloud import storage
from google.cloud import aiplatform
from google.oauth2 import service_account

# Load environment variables from .env file
load_dotenv()

# Initialize Google Cloud clients
def init_google_cloud():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        )
        
        # Initialize Storage client
        storage_client = storage.Client(credentials=credentials)
        
        # Initialize Vertex AI
        aiplatform.init(
            project=os.getenv('GOOGLE_CLOUD_PROJECT'),
            location=os.getenv('GOOGLE_CLOUD_REGION')
        )
        
        return storage_client
    except Exception as e:
        print(f"Error initializing Google Cloud: {e}")
        return None

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize cache
price_cache = {
    'price': None,
    'timestamp': None,
    'cache_duration': timedelta(minutes=1)
}

historical_cache = {
    'prices': None,
    'timestamp': None,
    'cache_duration': timedelta(minutes=5)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/price')
def get_price():
    try:
        # Your existing price fetching logic
        pass
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/historical')
def get_historical():
    try:
        # Your existing historical data logic
        pass
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/_ah/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
