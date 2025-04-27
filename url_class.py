import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_URL = "https://www.virustotal.com/api/v3/urls"

headers = {
    "accept": "application/json",
    "x-apikey": os.environ['API_KEY'],
    "content-type": "application/x-www-form-urlencoded"
}


class Url:
    def __init__(self, url):
        self.address_url = url
        self.results_list = []
        self.list_of_security_tools = []
        self.list_of_analysis_stats = []
        self.number_of_security_tools = 0

    def check_url_address(self):

        payload = {"url": self.address_url }

        response = requests.post(url=API_URL, data=payload, headers=headers)
        response_json = response.json()

        url_get = API_URL + "/" + response_json['data']['id'].split('-')[1]

        response_get = requests.get(url_get, headers=headers)
        response_get = response_get.json()

        self.list_of_security_tools = [ elm for elm in response_get['data']['attributes']['last_analysis_results']]

        self.results_list = { elm : {
            "method" : response_get['data']['attributes']['last_analysis_results'][elm]['method'],
            "category" : response_get['data']['attributes']['last_analysis_results'][elm]['category'],
            "result" : response_get['data']['attributes']['last_analysis_results'][elm]["result"]
        } for elm in response_get['data']['attributes']['last_analysis_results']}

        self.list_of_analysis_stats = {
            "malicious" : int(response_get['data']['attributes']['last_analysis_stats']['malicious']),
            "suspicious": int(response_get['data']['attributes']['last_analysis_stats']['suspicious']),
            "undetected" : int(response_get['data']['attributes']['last_analysis_stats']['undetected']),
            "harmless" : int(response_get['data']['attributes']['last_analysis_stats']['harmless']),
            "timeout" : int(response_get['data']['attributes']['last_analysis_stats']['timeout'])
        }

        self.number_of_security_tools = len(self.list_of_security_tools)


