# NotisendApi
Small python module for sending emails with [notisend.ru](https://app.notisend.ru/mailer) api

# Dependencies

```
sudo apt-get install python3 python3-pip
pip install requests
```

# Install

From git

```
pip install git+https://github.com/artem78/NotisendApi.git
```

# Usage

```python3
from notisend_api import NotisendApi

api = NotisendApi('Your API KEY here')

try:
    api.send_email('me@example.com',  # From email
                   'you@example.com', # To email
                   'Just testing',    # Subject
                   'hellow\nworld!')  # Message body (plain text)
    print('Successfully sent!')
except Exception as e:
    print('Failed! - ' + str(e))
```
