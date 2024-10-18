from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from fastapi import Request
import os
import requests
from github_linkedin_func.linkedin_api import LinkedInAPI


app = APIRouter()

LINKEDIN_CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID')
LINKEDIN_CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET')
LINKEDIN_REDIRECT_URI = os.getenv('LINKEDIN_REDIRECT_URI', 'http://localhost:8000/auth/linkedin/callback')

@app.get("/auth/linkedin")
async def auth_linkedin():
    try:
        authorization_url = (f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id="
                             f"{LINKEDIN_CLIENT_ID}&redirect_uri={LINKEDIN_REDIRECT_URI}"
                             f"&scope=r_liteprofile%20r_emailaddress%20w_member_social")
        return RedirectResponse(authorization_url)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating authorization URL: {str(e)}")

@app.get("/auth/linkedin/callback")
async def linkedin_callback(code: str):
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET,
    }
    try:
        response = requests.post(token_url, data=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        access_token = response.json().get('access_token')
        # Store the access token as needed (e.g., session, database, etc.)
        return {"access_token": access_token}

    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {str(http_err)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to obtain access token: {str(e)}")

@app.get("/linkedin/profile")
async def get_linkedin_profile(access_token: str):
    try:
        linkedin_api = LinkedInAPI(access_token)
        profile = linkedin_api.fetch_profile()
        skills = linkedin_api.fetch_skills()

        return {
            "profile": {
                "name": f"{profile.get('localizedFirstName')} {profile.get('localizedLastName')}",
                "headline": profile.get('headline'),
                "profile_url": f"https://www.linkedin.com/in/{profile.get('vanityName')}",
            },
            "skills": skills
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching LinkedIn profile: {str(e)}")