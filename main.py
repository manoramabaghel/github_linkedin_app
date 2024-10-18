# from fastapi import FastAPI, HTTPException
# from fastapi.responses import RedirectResponse
# from fastapi import Request
# from github_linkedin_func.linkedin_api import LinkedInAPI
# import os
# import requests
#
# app = FastAPI()
#
# LINKEDIN_CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID')
# LINKEDIN_CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET')
# LINKEDIN_REDIRECT_URI = os.getenv('LINKEDIN_REDIRECT_URI')
#
# @app.get("/auth/linkedin")
# async def auth_linkedin():
#     authorization_url = (f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id="
#                          f"{LINKEDIN_CLIENT_ID}&redirect_uri={LINKEDIN_REDIRECT_URI}"
#                          f"&scope=r_liteprofile%20r_emailaddress%20w_member_social")
#     return RedirectResponse(authorization_url)
#
#
# @app.get("/auth/linkedin/callback")
# async def linkedin_callback(code: str):
#     token_url = "https://www.linkedin.com/oauth/v2/accessToken"
#     payload = {
#         'grant_type': 'authorization_code',
#         'code': code,
#         'redirect_uri': LINKEDIN_REDIRECT_URI,
#         'client_id': LINKEDIN_CLIENT_ID,
#         'client_secret': LINKEDIN_CLIENT_SECRET,
#     }
#     response = requests.post(token_url, data=payload)
#     print(f"Received authorization code: {code}")
#     if response.status_code == 200:
#         access_token = response.json().get('access_token')
#         # Store the access token as needed (e.g., session, database, etc.)
#         return {"access_token": access_token}
#     else:
#         raise HTTPException(status_code=400, detail="Failed to obtain access token.")
#
# @app.get("/linkedin/profile")
# async def get_linkedin_profile(access_token: str):
#     linkedin_api = LinkedInAPI(access_token)
#     profile = linkedin_api.fetch_profile()
#     skills = linkedin_api.fetch_skills()
#
#     return {
#         "profile": {
#             "name": f"{profile.get('localizedFirstName')} {profile.get('localizedLastName')}",
#             "headline": profile.get('headline'),
#             "profile_url": f"https://www.linkedin.com/in/{profile.get('vanityName')}",
#         },
#         "skills": skills
#     }
#
#
#
#
# # # Main application logic
# # from github_linkedin_func.github_api import GitHubAPI
# # from github_linkedin_func.linkedin_api import LinkedInAPI
# # from tabulate import tabulate
# #
# # # Replace with your tokens
# # GITHUB_TOKEN = 'your_github_token_here'
# # LINKEDIN_TOKEN = 'your_linkedin_access_token_here'
# #
# #
# # def main():
# #     github_api = GitHubAPI(GITHUB_TOKEN)
# #     linkedin_api = LinkedInAPI(LINKEDIN_TOKEN)
# #
# #     try:
# #         repo_owner = input("Enter GitHub repo owner: ")
# #         repo_name = input("Enter GitHub repo name: ")
# #
# #         # Fetch and display GitHub files
# #         files = github_api.fetch_files(repo_owner, repo_name)
# #         file_info = [(f['name'], f['size'], f['last_modified']) for f in files]
# #         print(tabulate(file_info, headers=["Filename", "Size", "Last Modified"]))
# #
# #         selected_file = input("Enter the filename to view commit history: ")
# #         commit_history = github_api.fetch_commit_history(repo_owner, repo_name, selected_file)
# #         print(tabulate(
# #             [(commit['sha'], commit['commit']['committer']['name'], commit['commit']['committer']['date']) for commit in
# #              commit_history], headers=["Commit SHA", "Author", "Date"]))
# #
# #     except Exception as e:
# #         print(f"Error: {e}")
# #
# #     try:
# #         # Fetch and display LinkedIn profile
# #         profile = linkedin_api.fetch_profile()
# #         print(f"Name: {profile['localizedFirstName']} {profile['localizedLastName']}")
# #         print(f"Headline: {profile['headline']}")
# #
# #         # Fetch and display LinkedIn skills
# #         skills = linkedin_api.fetch_skills()
# #         print("Top Skills:")
# #         for skill in skills[:5]:
# #             print(f"- {skill['name']} (Endorsements: {skill['endorsementCount']})")
# #     except Exception as e:
# #         print(f"Error: {e}")
# #
# #
# # if __name__ == "__main__":
# #     main()
# #
