"""
Author: Vijay Kumar Singh
Date: 9 Jan 2025
Description: Fetching data from OpenWeather and saving it to AWS-S3 bucket.
Version: 1.0.0
"""

import os
import boto3
import requests
import json
import datetime

import os
import requests 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

city = "London"
api_key = os.getenv("API_KEY")
# Debugging step to make sure the API key is being read from the environment
print(f"API_KEY from environment: {api_key}")
if not api_key:
    print("API key not found. Please check the .env file.")
    exit()

# response.get(api.openweathermap.org/data/2.5/weather)
base_url = f"https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key
}
response = requests.get(base_url, params=params)
r = response.status_code
print(r)

if r == 401:
    print("Error 401: Unauthorized. Check your API key.")
else:
    print(f"Response status code: {r}")
