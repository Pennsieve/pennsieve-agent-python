import requests
import json
from userProfile import UserProfile

class PennsieveAPI(object):


    def __init__(self, stub):
#        self.sessionToken=credentials['sessionToken']
#        self.organizationId=credentials['organizationId']
        self.stub=stub
        self.user=UserProfile(self.stub)
        self.headers = { "Content-Type" : "application/json",
                        "Accept" : "application/json; charset=utf-8",
                        "Authorization" : "Bearer " + self.user.credentials['session_token'],
                        "X-ORGANIZATION-ID" : self.user.credentials['organization_id']}


    def getUser(self):
        return self.user.whoami()




    def connect(self):
        self.stub


    def get(self, url, **kwargs):
        print(kwargs)
        if url.startswith('/'):
            url=self.user.api_host + url
        print(url)
        if 'headers' not in kwargs:
            headers=self.headers
        else:
            headers=kwargs['headers']
        try:
            print("HEADERS: "+ str(headers))
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other excpetion occurred: {err}')
        else:
            return response.json() #content.decode('utf-8'))





"""
    def get(self, endpoint='https://api.pennsieve.io/datasets/'):
        try:
            print(str(headers))
            response = requests.get(endpoint, headers=self.headers)
            r =json.loads(response.content.decode('utf-8'))
            print(str(r))
            print(response.raise_for_status())
        except requests.exceptions.HTTPError as err:
            raise

"""

"""
headers={'Authorization': 'access_token myToken'})

# Get all manifests
  "url = 'https://api.pennsieve.io/discover/datasets'\n",
    "headers={\"content-type\":\"text\", 'Accept':'*/*'}\n",
    "response=requests.get(url, headers=headers)\n",
    "datasets=json.loads(response.content.decode('utf-8'))\n",
    "offset=10\n",
    "file_offset=10\n",
    "limit=offset\n",
    "\n",
    "all_items={}  #stores datasetId->doi\n",
    "#num_files={}  #\n",
    "filelist=[]   #a list of all files from public datasets\n",
"""
