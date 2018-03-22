import sys
import unittest

from bing_api.clients import BingWebSearch


class BingWebSearchV7TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'

    def test_search(self):
        bing_web_search_client = BingWebSearch(
            self.search_url,
            self.subscription_key
        )
        search_result = bing_web_search_client.search(
            'the cognitive dissonance'
        )


if __name__ == '__main__':
    BingWebSearchV7TestCase.subscription_key = sys.argv.pop(None)
    unittest.main()
