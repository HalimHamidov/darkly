Unrestricted File Upload

Переходим на страницу http://192.168.56.110/?page=upload.

Мы собираемся заставить front принимать php-файл с помощью curl. 
Поскольку в бэкэнде нет проверки файла, наш пустой php файл пройдет. 

touch script.php && curl -F "Upload=" -F "uploaded=@script.php;type=image/jpeg" http://192.168.56.110/index.php?page=upload > script.html

Откроем страничку index.html и мы можем увидеть флаг.


Это действительно опасно. С помощью выгрузки изображения можно отправлять php-запрос на веб-сайт и бэкэнд.

Рекомендации:

* Рекомендуется ознакомиться со следующей статьей
https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload#Prevention_Methods_.28Solutions_to_be_more_secure.29

* Разрешенные для загрузки типы файлов должны быть доступны только тем, кому необходимы для выполнений своих обязанностей? в противном случае ограничить права.
Никогда не принимайте файлы  без фильтра расширений файлов и  разрешений.

* Проверить в бэкэнде тип и заголовок файла, а не только во фронтэнде.
Web Server Protection (WAF) Rule
* Убедитесь, что файлы конфигурации, такие как «.htaccess» или «web.config», нельзя заменить с помощью загрузчиков файлов.
* Используйте методы защиты от подделки межсайтовых запросов.(Cross Site Request Forgery protection methods)

Reference:
       -F, --form <name=content>
              (HTTP)  This  lets curl emulate a filled-in form in which a user
              has pressed the submit button. This causes  curl  to  POST  data
              using  the  Content-Type  multipart/form-data  according  to RFC
              2388. This enables uploading of binary files etc. To  force  the
              'content'  part  to  be  a  file, prefix the file name with an @
              sign. To just get the content part from a file, prefix the  file
              name  with  the symbol <. The difference between @ and < is then
              that @ makes a file get attached in the post as a  file  upload,
              while  the  <  makes  a text field and just get the contents for
              that text field from a file.

              Example: to send an image to a server, where  'profile'  is  the
              name of the form-field to which portrait.jpg will be the input:

               curl -F profile=@portrait.jpg https://example.com/upload.cgi

              To read content from stdin instead of a file, use - as the file-
              name. This goes for both @ and <  constructs.  Unfortunately  it
              does  not support reading the file from a named pipe or similar,
              as it needs the full size before the transfer starts.

              You can also  tell  curl  what  Content-Type  to  use  by  using
              'type=', in a manner similar to:

               curl -F "web=@index.html;type=text/html" example.com

              or

               curl -F "name=daniel;type=text/foo" example.com

              You  can  also explicitly change the name field of a file upload
              part by setting filename=, like this:

               curl -F "file=@localfile;filename=nameinpost" example.com

              If filename/path contains ',' or ';', it must be quoted by  dou-
              ble-quotes like:

               curl   -F  "file=@\"localfile\";filename=\"nameinpost\""  exam-
              ple.com

              or

               curl -F 'file=@"localfile";filename="nameinpost"' example.com

              Note that if a filename/path is  quoted  by  double-quotes,  any
              double-quote or backslash within the filename must be escaped by
              backslash.

              See further examples and details in the MANUAL.

              This option can be used multiple times.

              This option overrides _-_d_, _-_-_d_a_t_a and _-_I_, _-_-_h_e_a_d and _-_-_u_p_l_o_a_d.



