# BingSearchClient
Simple search client for Bing API V7. Details description: <br/>
https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-web-api-v7-reference

<p>Example:</p>
<p>from bing_api.clients import BingWebSearch</p>

<p>search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'<br/>
subscription_key = 'your subscription key for bing'</p>

<p>bing_web_search_client = BingWebSearch(search_url, subscription_key)<br/>
search_result = bing_web_search_client.search('the cognitive dissonance')</p>
