from time import time
import requests
import random
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

headers = {
    'authority': 'kahoot.it',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://kahoot.it/',
    'accept-language': 'en-US,en;q=0.9',
}

def genRandomPin():
    if random.randint(0,1) == 1:
        return random.randint(100000,999999)
    else:
        return random.randint(1000000,9999999)

while True:
    pin = genRandomPin()
    response = requests.get(f'https://kahoot.it/reserve/session/{pin}/?1649783470488', headers=headers)
    if response.status_code == 404:
        #print(f"{bcolors.FAIL} {str(response.status_code)}   :   {str(pin)}{bcolors.ENDC}")
        pass
    else:
        print(f"{bcolors.OKGREEN} FOUND :   {str(pin)}{bcolors.ENDC}")
