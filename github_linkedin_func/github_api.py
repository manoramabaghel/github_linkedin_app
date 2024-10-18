# GitHub API integration
import requests

class GitHubAPI:
    BASE_URL = "https://api.github.com/"
    def __init__(self, token: str):
        self.token = token
        # self.api_url = 'https://api.github.com'

    def fetch_files(self, repo_owner, repo_name):
        try:
            headers = {'Authorization': f'token {self.token}'}
            url = f"{self.BASE_URL}repos/{repo_owner}/{repo_name}/contents"
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()  # Raise an error for HTTP errors

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Provide HTTP error message
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors

    def fetch_commit_history(self, repo_owner, repo_name, file_path):
        try:
            repo_name = repo_name.strip('/')
            headers = {'Authorization': f'token {self.token}'}
            url = f"{self.BASE_URL}/repos/{repo_owner}/{repo_name}/commits?path={file_path}"
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Provide HTTP error message
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle other request errors
