# Tests for LinkedIn API
import unittest
from github_linkedin_func.linkedin_api import LinkedInAPI

class TestLinkedInAPI(unittest.TestCase):
    def setUp(self):
        self.linkedin_api = LinkedInAPI('your_linkedin_access_token_here')  # Use a valid test token

    def test_fetch_profile(self):
        profile = self.linkedin_api.fetch_profile()
        self.assertIn('localizedFirstName', profile)

    def test_fetch_skills(self):
        skills = self.linkedin_api.fetch_skills()
        self.assertIsInstance(skills, list)

if __name__ == '__main__':
    unittest.main()
