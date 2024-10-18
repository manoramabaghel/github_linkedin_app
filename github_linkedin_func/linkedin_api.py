# LinkedIn API integration
import requests

class LinkedInAPI:
    BASE_URL = "https://api.linkedin.com/v2/"
    def __init__(self, access_token):
        self.access_token = access_token
        # self.api_url = 'https://api.linkedin.com/v2'

    def fetch_profile(self):
        try:
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.get(self.BASE_URL + "me", headers=headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Provide HTTP error message
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors

    def fetch_skills(self):
        try:
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.get(self.BASE_URL + "me/skils", headers=headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Provide HTTP error message
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors
