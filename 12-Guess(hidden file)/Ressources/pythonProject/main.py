import requests
from bs4 import BeautifulSoup

readme = 'README'
is_href = 'href'
go_back = '../'

'''
    Поиск по ссылкам, на что указывает тэг <a>, который может содержать
    разные атрибуты, включая href - href=True
    Начинается 
'''
result_file = open('result.txt', 'a')
wrong_message = [
    "b\"Non ce n\'est toujours pas bon ...\\n\"",
    "b\'Demande \\xc3\\xa0 ton voisin du dessus  \\n\'",
    "b\'Demande \\xc3\\xa0 ton voisin de droite  \\n\'",
    "b\'Demande \\xc3\\xa0 ton voisin de gauche  \\n\'",
    "b\'Toujours pas tu vas craquer non ?\\n\'",
    "b\'Demande \\xc3\\xa0 ton voisin du dessous \\n\'",
    "b\"Tu veux de l\'aide ? Moi aussi !  \\n\""
]

def scan_folder(result):
    scrap = BeautifulSoup(result.content, features="html.parser")
    for tag_a in scrap.find_all('a', href=True):
        if tag_a[is_href] == go_back:
            continue
        if tag_a[is_href] == readme:
            text = str(requests.get(result.request.url + tag_a[is_href]).content)
            if text in wrong_message:
                continue
            result_file.write(str(text) + '\n')

        else:
            next_address = result.request.url + tag_a['href']
            scan_folder(requests.get(next_address))

result = requests.get("http://192.168.56.101/.hidden/")
scan_folder(result)
result_file.close()
print("Finished. Please, check result in 'result.txt' file")
