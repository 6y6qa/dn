import os
import requests
import time
import hashlib
import random
from colorama import Fore,Back
os.system('clear')
os.system('rm -fr dn')
rangakan=(Fore.BLUE,Fore.CYAN,Fore.GREEN,Fore.LIGHTBLACK_EX,Fore.RED,Fore.YELLOW)
rang=random.choice(rangakan)
logo=rang+'''

     ___                          ___                                     ___  
    (   )                        (   )                                   (   ) 
  .-.| |   ___ .-.        ,--.    | |   ___    ___  ___   ___ .-.      .-.| |  
 /   \ |  (   )   \      /   |    | |  (   )  (   )(   ) (   )   \    /   \ |  
|  .-. |   |  .-. .     / .' |    | |  ' /     | |  | |   | ' .-. ;  |  .-. |  
| |  | |   | |  | |    / / | |    | |,' /      | |  | |   |  / (___) | |  | |  
| |  | |   | |  | |   / /  | |    | .  '.      | |  | |   | |        | |  | |  
| |  | |   | |  | |  /  `--' |-.  | | `. \     | |  | |   | |        | |  | |  
| '  | |   | |  | |  `-----| |-'  | |   \ \    | |  ; '   | |        | '  | |  
' `-'  /   | |  | |        | |    | |    \ .   ' `-'  /   | |        ' `-'  /  
 `.__,'   (___)(___)      (___)  (___ ) (___)   '.__.'   (___)        `.__,'   
                                                                               
                                                                               
'''
def login():
    os.system('clear')
    print(logo)
    user=input('YOUR USER NAME : ')
    print(Fore.LIGHTBLUE_EX+'LODING...')
    time.sleep(5)
     
    file=requests.get('https://github.com/6y6qa/dn/raw/main/user.txt').text
    if f'{user}' not in file:
        print(Back.LIGHTRED_EX+'NO USER FOUND')
    else:
         print('FORGET PASSWORD? ENTER 0')
         mrx=input(Fore.LIGHTMAGENTA_EX+'YOUR PASSWORD : ')
         if user =='mrx' and mrx=='mrx1270':
             
             print(Fore.GREEN+'SUCCESSFUL')
             print('LODING...')
             time.sleep(5)
             os.system('cmatrix')
         if mrx =='0':
             print('SEND CHAT FOR ADMIN TELEGRAM : @i4m_mrx')
         else:
             print(Back.LIGHTRED_EX+'PASSWORD INCORRECT')
           
       

def singup():
    os.system('clear')
    print(logo)
    user=input('YOUR USER NAME : ')
    email=input('YOU EMAIL : ')
    print('LODING...')
    time.sleep(15)
    file=requests.get('https://github.com/6y6qa/dn/raw/main/user.txt').text
    if f'{user}' in file:
        print('USER ALREADY EXISTS ')
    else:
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()
        print(Fore.LIGHTGREEN_EX+'SUCCESSFUL SINUP')
        print(f'YOUR PASSWORD : {h2}')
        token='6073444393:AAH8kU845zl8pSDMuptNqGPcmmN7EWHTgFw'
        chat_id='-1001977949065'
        id='5538462835'
        photo_path = 'kurd.png'
        import datetime
        halo = datetime.date.today()
        sal=halo.year
        mang=halo.month
        rozh=halo.day
        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime("%I:%M %p")
        kat=(f"{sal}/{mang}/{rozh} {formatted_time}")
        text=f'''
        ئەندامی نوێ
        ناو : {user}
        کاتی خۆتۆمارکردن : {kat}
        پلە : میوان'''
        halom=f'''
        user : {user}
        email : {email}
        password : {h2}'''
        url1 = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {
            'chat_id': id,
            'text': halom
        }
        response1 = requests.get(url1, params=params)

        url = f'https://api.telegram.org/bot{token}/sendPhoto'
        with open(photo_path, 'rb') as photo:
            response = requests.post(url, data={'chat_id': chat_id, 'caption': text}, files={'photo': photo})
        halo=input('ENTER TO LOGIN : ')
        login()




print(logo)
print(rang+'1-LOGIN TO DN4KURD')
print(rang+'2-SINGUP IN DN4KURD')
halo=input('SELECT : ')
if halo=='1':

    login()
if halo=='2':
    singup()


