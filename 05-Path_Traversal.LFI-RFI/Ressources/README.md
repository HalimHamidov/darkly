Directory traversal attack / Path Traversal /
File Path Traversal and File Inclusions(LFI / RFI)

https://owasp.org/www-community/attacks/Path_Traversal

https://en.wikipedia.org/wiki/Directory_traversal_attack#Example

Атака с обходом каталога (или обходом пути) использует недостаточную проверку безопасности или дезинфекцию предоставленных пользователем имен файлов, так что символы, представляющие «переход к родительскому каталогу», передаются в API файловой системы операционной системы. Уязвимое приложение может быть использовано для получения несанкционированного доступа к файловой системе.


Обход каталога также известен как ../ (dot dot slash) атака, directory climbing, и backtracking. Некоторые формы этой атаки также известны как атаки канонизации (процесс преобразования данных в одно возможное представление).

Файл пароля Unix 
https://ru.wikipedia.org/wiki/%2Fetc%2Fpasswd

/etc/passwd (от англ. password — пароль) — файл, содержащий в текстовом формате список пользовательских учётных записей (аккаунтов).

Является первым и основным источником информации о правах пользователя операционной системы. Существует в большинстве версий и вариантов UNIX-систем. Обязан присутствовать в POSIX-совместимой операционной системе.

Как найти эксплойт: 
https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include.md

в адресной строке добавляем "/?page=../etc/passwd". 
Предупреждающее сообщение сообщает, что мы приближаемся к эксплойту.

продолжаем добавлять "../", пока предупреждающее сообщение не выдаст вам флаг. 
http://192.168.56.108/?page=../../../../../../../etc/passwd

Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 


Как это исправить: 

* Защитить свои файлы. 

* Запретить доступ пользователей к конфиденциальным данным или каталогам.

Рекомендации OWASP:

* How to protect yourself

* Prefer working without user input when using file system calls

* Use indexes rather than actual portions of file names when templating or using language files (ie value 5 from the user submission = Czechoslovakian, rather than expecting the user to return “Czechoslovakian”)

* Ensure the user cannot supply all parts of the path – surround it with your path code

* Validate the user’s input by only accepting known good – do not sanitize the data

* Use chrooted jails and code access policies to restrict where the files can be obtained or saved to

* If forced to use user input for file operations, normalize the input before using in file io API’s, such as normalize().