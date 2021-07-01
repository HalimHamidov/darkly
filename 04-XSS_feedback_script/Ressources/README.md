
Нажимаем на оставить фидбек и если вводим теги a, p или script без <> в область комментариев, то получаем флаг. Это и есть HTML инъекция.

http://192.168.56.108/?page=feedback
Предполагается, что можно вставить код в заголовок или поле комментария. 
XSS считается сохраненным, поскольку весь введенный код постоянно остается на странице обратной связи и выполняется при каждой перезагрузке. 
Это немного специфично, потому что для получения флага нам нужно было поместить одно из этих ключевых тегов: a, script, p в одно из двух полей. 

Обычно, XSS должна содержать html и / или javascript, но здесь все, что содержится внутри тегов, игнорируется.

Описание: Чем опасна:
https://habr.com/ru/company/simplepay/blog/258499/

XSS уязвимость Что такое XSS?
XSS — это уязвимость веб-страниц, возникающая в результате попадания в них пользовательских JS-скриптов.

Межсайтовый скриптинг – XSS (Cross Site Scripting)

Межсайтовый скриптинг – еще одна ошибка валидации пользовательских данных, которая позволяет передать JavaScript код на исполнение в браузер пользователя. Атаки такого рода часто также называют HTML-инъекциями, ведь механизм их внедрения очень схож с SQL-инъекциями, но в отличие от последних, внедряемый код исполняется в браузере пользователя. Чем это чревато?

Во-первых, злоумышленник может украсть вашу сессионную cookie, последствия чего были описаны во втором пункте, буквально парой абзацев выше. Нужно отметить, что далеко не все серверы приложений уязвимы к данному типу атак, об этом мы отдельно поговорим в пункте под номером 5.

Во-вторых, могут быть украдены данные, вводимые в формы на зараженной странице. А это могут быть конфиденциальные персональные данные, или, что еще хуже, данные кредитной карты вместе с CVC-кодом.

В третьих, через JavaScript можно изменять данные, расположенные на странице, например, там могут быть реквизиты для банковского перевода, которые злоумышленник с удовольствием подделает и заменит подставными.

Решение:

[Рекомендации OWASP:](https://owasp.org/www-community/attacks/xss/)

How to Protect Yourself
The primary defenses against XSS are described in the [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).

Also, it’s crucial that you turn off HTTP TRACE support on all web servers. An attacker can steal cookie data via Javascript even when document.cookie is disabled or not supported by the client. This attack is mounted when a user posts a malicious script to a forum so when another user clicks the link, an asynchronous HTTP Trace call is triggered which collects the user’s cookie information from the server, and then sends it over to another malicious server that collects the cookie information so the attacker can mount a session hijack attack. This is easily mitigated by removing support for HTTP TRACE on all web servers.

The OWASP ESAPI project has produced a set of reusable security components in several languages, including validation and escaping routines to prevent parameter tampering and the injection of XSS attacks. In addition, the OWASP WebGoat Project training application has lessons on Cross-Site Scripting and data encoding.

* Разработчики должны внедрить белый список допустимых входных данных, и если это невозможно, то нужно организовать проверки входных данных. Более того, данные, введенные пользователем, должны быть отфильтрованы 

* Output encoding является наиболее надежным решением для борьбы с XSS, поскольку оно принимает код скрипта и преобразует его в обычный текст 

* Межсетевой экран WAF должен активирован, поскольку он защищает приложение от XSS-атак 

* Использование флагов HTTPOnly на файлах cookie 

* Разработчики могут применить политику безопасности контента (CSP) для снижения возможности появления любых уязвимостей XSS

 Источник: https://cisoclub.ru/rukovodstvo-po-osushhestvleniyu-cross-site-scripting-xss/

От XSS уязвимости вас могут защитить две основные функции:

strip_tags() - удаляет из строки все HTML-теги, кроме разрешённых.

htmlspecialchars() - заменяет все спецсимволы на их HTML-аналоги (< заменяется на &lt; и т.д.)
В принципе, если проверять переданные пользователем переменные (будь то форма или простой запрос через адресную строку), то этих функций обычно хватает. Однако я бы посоветовал ещё проверять на наличие двоеточия (:), процента (%), слэшей (/ и \), а не только те, что в htmlspecialchars - &, ', ", <, >. Это уже делается функциями с регулярными выражениями - обычно preg_replace.



