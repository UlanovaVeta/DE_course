cat <<EOL > access.log
192.168.1.1 - - [28/Jul/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [28/Jul/2024:12:35:56 +0000] "POST /login HTTP/1.1" 200 567
192.168.1.3 - - [28/Jul/2024:12:36:56 +0000] "GET /home HTTP/1.1" 404 890
192.168.1.1 - - [28/Jul/2024:12:37:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.4 - - [28/Jul/2024:12:38:56 +0000] "GET /about HTTP/1.1" 200 432
192.168.1.2 - - [28/Jul/2024:12:39:56 +0000] "GET /index.html HTTP/1.1" 200 1234
EOL

{
	echo "Отчет о логе веб-сервера"
	echo "========================================"
	echo "Общее количество запросов: $(wc -l < $"access.log")"
	echo "Количество уникальных IP-адресов: $(awk '{print $1}' $"access.log" | sort -u | wc -l)"
	echo "Количество запросов методом GET: $(awk '$6 == "\"GET" {count++} END {print count+0}' $"access.log")"
	echo "Количество запросов методом POST: $(awk '$6 == "\"POST" {count++} END {print count+0}' $"access.log")"
	echo "Количество запросов методом PUT: $(awk '$6 == "\"PUT" {count++} END {print count+0}' $"access.log")"
	echo "Количество запросов методом DELETE: $(awk '$6 == "\"DELETE" {count++} END {print count+0}' $"access.log")"
	echo "Самый популярный запрос: $(awk '{print $7}' $"access.log" | sort | uniq -c | sort -nr | head -n 1)"
} > "report.txt"
echo "Отчет успешно создан и сохранен в файл report.txt"