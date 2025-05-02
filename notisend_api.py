import requests
from urllib.parse import urljoin

class NotisendApi:
    def __init__(self, api_token):
        self.api_token = api_token
        self.__api_base_url = 'https://api.notisend.ru/v1/'
    
    def send_email(self, sender, recipient, subject, msg):
        url =  urljoin(self.__api_base_url, 'email/messages')
        
        headers = {
            'Authorization': 'Bearer ' + self.api_token 
        }
        
        json_data = {
           "from_email": sender,
           #"from_name": "John Doe",
           "to": recipient,
           "subject": subject,
           "text": msg#,
           #"html": "<h1>Hello, Bob!</h1>",
           #"payment": "credit",
           #"smtp_headers": {
           #  "Client-Id": "123"
           #}
        }
        
        resp = requests.post(url, json=json_data, headers=headers)
        if resp.status_code > 299:
            raise Exception(str(resp.json().get("errors")))
        