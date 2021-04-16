import requests
import string
import random
from random import randint
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
#//////////////////////////////////////////////
print('\033[31m' +"###################################################################")
print('\033[31m' +"#")
print('\033[31m' +"#"+f"{Fore.GREEN}                WELCOME TO HELL code by the EREBUS")
print('\033[31m' +"#")
print('\033[31m' +"###################################################################")
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
for i in range(3):
    randsize =randint(8,24)
    username=id_generator(randsize)
    password=id_generator(randsize)
    #nssifto requests
    files = {
    'email': (None, '{}@gmail.com'.format(username)),
    'password': (None, password),
}
    print('\033[31m' +"=============================")
    print("request number : {}".format(i))
    print('\033[31m' +"Email:{}\nPassword:{}".format('{}@gmail.com'.format(username),password))
    response = requests.post('https://smikta.info/nolive.php', files=files)