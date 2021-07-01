Нажми на значение в конце страницы - © BornToSec
Тем самым мы зайдём по адресу http://192.168.56.108/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
If we inspect the page we will find the text where we can find hints.
We may curl it and save the page into flag01.html and when we open it we can see the flag on front page firstly.

Если происследовать страницу, то найдём текс, где можно найти подсказку. Мы можем воспользоваться функцией curl и сохранить страницу в flag01.html, где его откроем и увидим флаг.

Флаг -А означает запустить через настоящий браузер.
Флаг -е говорит о том по какой ссылке проводить соединение.
Вход идёт из "https://www.nsa.gov/" в http://192.168.56.108 через браузер ft_bornToSec"

➜  ~ curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://192.168.56.108/\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c > flag01.html

The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

Почему это опасно?
Выводить User Agent может вызывать проблемы с XSS. Его выполнение может разрешить удаленное выполнение кода на языке, используемом на стороне сервера. Проверка реферера может предотвратить множественные проблемы безопасности, такие как RFI (включение удаленного файла) или CSRF (подделка межсайтовых запросов).

чтобы решить эту проблему, нам нужно добавить токен в params

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