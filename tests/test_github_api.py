# Tests for GitHub API
import unittest
from github_linkedin_func.github_api import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.github_api = GitHubAPI('your_github_token_here')  # Use a valid test token

    def test_fetch_files(self):
        files = self.github_api.fetch_files('owner', 'repo')  # Replace with valid test values
        self.assertIsInstance(files, list)

    def test_fetch_commit_history(self):
        commit_history = self.github_api.fetch_commit_history('owner', 'repo', 'file_path')  # Replace with valid test values
        self.assertIsInstance(commit_history, list)

if __name__ == '__main__':
    unittest.main()
