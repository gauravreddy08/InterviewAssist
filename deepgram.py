import requests
from dotenv import load_dotenv
import os
class Deepgram():
    def __init__(self):
        load_dotenv(override=True)
        DEEPGRAM_API = os.getenv("DEEPGRAM_API_KEY")

        self.url = "https://api.deepgram.com/v1/listen"

        # Define the headers for the HTTP request
        self.headers = {
            "Authorization": f"Token {DEEPGRAM_API}",
            "Content-Type": "audio/*"
        }
    
    def call(self, filepath="output.mp3"):
        print("STT in action...")
        # Get the audio file
        with open(filepath, "rb") as audio_file:
            # Make the HTTP request
            response = requests.post(self.url, headers=self.headers, data=audio_file)
        if response.status_code==200:
            return response.json()['results']['channels'][0]['alternatives'][0]['transcript']