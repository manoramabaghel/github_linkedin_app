from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from github_linkedin_func.github_api import GitHubAPI
from github_linkedin_func.linkedin_api import LinkedInAPI

app = APIRouter()

# Replace with your GitHub token
GITHUB_TOKEN = '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'
github_api = GitHubAPI(GITHUB_TOKEN)


class FileInfo(BaseModel):
    name: str
    # size: str
    # last_modified: str
    size: int
    last_modified: str = Field(default='N/A')  # Default value if not provided
    contributors: list[str]  # List of contributor usernames

class CommitInfo(BaseModel):
    sha: str
    node_id: str
    author: str
    url: str
    date: str
    message: str


    @classmethod
    def from_commit(cls, commit):
        return cls(
            sha=commit['sha'],
            node_id=commit['node_id'],
            author=commit['commit']['committer']['name'],
            url=commit['url'],
            date=commit['commit']['committer']['date'],
            message=commit['commit']['message']
        )
@app.get("/search", response_model=list[FileInfo])
async def search(owner: str, repo: str, search: str = ""):
    if not owner or not repo:
        raise HTTPException(status_code=400, detail="Repository owner and name are required.")

    try:
        files = github_api.fetch_files(owner, repo)

        # Filter files based on search query
        if search:
            files = [file for file in files if search.lower() in file['name'].lower()]

        # Prepare the response data
        file_info = []

        for f in files:
            # Initialize last_modified and contributors
            last_modified = 'N/A'
            contributors = []
            if f['type'] == 'file':
                # Get last modified date by fetching commit history for each file
                commit_history = github_api.fetch_commit_history(owner, repo, f['name'])
                if commit_history and 'commit' in commit_history[0]:
                    last_modified = commit_history[0]['commit']['author']['date']
                    contributors = [commit['commit']['author']['name'] for commit in commit_history]

                # last_modified = commit_history[0]['commit']['author']['date'] if commit_history else 'N/A'
                # contributors = [commit['commit']['author']['name'] for commit in commit_history]

            file_info.append(
                FileInfo(
                    name=f['name'],
                    size=int(f.get('size', 0)),  # Ensure size is an integer
                    last_modified=last_modified,
                    contributors=contributors
                )
            )

        return file_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/commits", response_model=list[CommitInfo])
async def get_commit_history(owner: str, repo: str, file_path: str):
    if not owner or not repo or not file_path:
        raise HTTPException(status_code=400, detail="Owner, repo, and file_path are required.")

    try:
        commit_history = github_api.fetch_commit_history(owner, repo, file_path)
        return [CommitInfo.from_commit(commit) for commit in commit_history]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# if __name__ == '__main__':
#     import uvicorn
#
#     uvicorn.run(app, host="127.0.0.1", port=8000)
