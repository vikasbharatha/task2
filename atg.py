
import unittest
import requests

class TestAtgWorld(unittest.TestCase):
    def test_website_loads_successfully(self):
        url = "https://www.atg.world"
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            print(f"Website {url} loaded successfully!")
        except requests.RequestException as e:
            self.fail(f"Failed to load website {url}: {e}")

if __name__ == "__main__":
    unittest.main()