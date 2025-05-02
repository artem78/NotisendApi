# NotisendApi
Small python module for sending emails with notisend.ru api

# Dependencies

```
sudo apt-get install python3
pip install requests
```

# Usage

```
from notisend_api import NotisendApi

api = NotisendApi('Your API KEY here')

try:
    api.send_email('me@example.com',  # From email
                   'you@example.com', # To email
                   'Just testing',    # Subject
                   'hellow\nworld!')  # Message body (plain text)
except Exception as e:
    print('Failed! - ' + str(e))
```
