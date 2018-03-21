import requests
from metaclasses import Singleton


class BingWebSearch(metaclass=Singleton):
    def __init__(self, search_url, subscription_key):
        self.search_url = search_url
        self.subscription_key = subscription_key

    def search(self, search_term, **additional_parameters):
        """
        Main method for web search by Bing API
        :param search_term:
        :param additional_parameters:
        :return:
        """
        headers, search_parameters = self._prepare_search_parameters(
            search_term,
            **additional_parameters
        )
        search_result = self._search(headers, search_parameters)

        return search_result

    def _prepare_search(self, search_term, **additional_parameters):
        """
        Method for prepare headers and search parameters
        :param search_term:
        :param additional_parameters:
        :return:
        """
        additional_headers = additional_parameters.get('headers', {})
        headers = self._prepare_headers(**additional_headers)

        additional_search_parameters = additional_parameters.get(
            'search', {}
        )
        search_parameters = self._prepare_search_parameters(
            search_term,
            **additional_search_parameters
        )

        return headers, search_parameters

    def _prepare_headers(self, **additional_headers):
        """
        Method for prepare headers
        :param additional_headers:
        :return:
        """
        headers = {'Ocp-Apim-Subscription-Key': self.subscription_key}
        if additional_headers:
            additional_headers.pop('Ocp-Apim-Subscription-Key', None)
            headers.update(additional_headers)

        return headers

    @staticmethod
    def _prepare_search_parameters(search_term, **additional_parameters):
        """
        Method for prepare search parameters
        :param search_term:
        :param additional_parameters:
        :return:
        """
        search_parameters = {
            'q': search_term,
            'textFormat': 'HTML'
        }
        if additional_parameters:
            additional_parameters.pop('q', None)
            search_parameters.update(additional_parameters)

        return search_parameters

    def _search(self, headers, search_parameters):
        """
        Internal method for search by Bing API
        :param headers:
        :param search_parameters:
        :return:
        """
        response = requests.get(
            self.search_url,
            headers=headers,
            params=search_parameters
        )
        response.raise_for_status()

        return response.json()
