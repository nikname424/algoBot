import requests
from config import token
 

def send_application(user_id, token, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': user_id, 
        'text': message
    }
    res = requests.post(url=url, data=data)
    print(res.json())

#message = 'Новая заявка!\nИмя -  \nВозраст -  \nИнтересующий курс -   \nНомер родителя  -    \nЗапись на курс - \nПОРА РАБОТАТЬ!  '
#send_application(user_id=5500790836, token=token, message=message)
