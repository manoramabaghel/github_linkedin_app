from fastapi import FastAPI
from github_linkedin_func.github_api import GitHubAPI
from github_linkedin_func.linkedin_api import LinkedInAPI
from routers.github_routes import app as github_router
from routers.linkedin_router import app as linkedin_router

app = FastAPI()

# Replace with your GitHub token
GITHUB_TOKEN = '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'
github_api = GitHubAPI(GITHUB_TOKEN)

# Linkedin_Token = ''



# Include the GitHub router
app.include_router(github_router)

# Include the LinkedIn router
app.include_router(linkedin_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
