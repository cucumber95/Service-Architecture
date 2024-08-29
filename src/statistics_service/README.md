## Запуск

```
docker-compose build
docker-compose up
```

## Примеры

Отправка лайка / просмотра:

```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"taskId": 1}' 'localhost:8090/statistics/send_like'
```
```
*   Trying 127.0.0.1:8090...
* Connected to localhost (127.0.0.1) port 8090 (#0)
> POST /statistics/send_like HTTP/1.1
> Host: localhost:8090
> User-Agent: curl/7.81.0
> Accept: */*
> Content-type: application/json
> Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ
> Content-Length: 13
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.3 Python/3.8.19
< Date: Thu, 20 Jun 2024 20:45:14 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 61
< Connection: close
< 
Запрос о лайке успешно отправлен
* Closing connection 0
```
```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"taskId": 1}' 'localhost:8090/statistics/send_view'
```
```
*   Trying 127.0.0.1:8090...
* Connected to localhost (127.0.0.1) port 8090 (#0)
> POST /statistics/send_view HTTP/1.1
> Host: localhost:8090
> User-Agent: curl/7.81.0
> Accept: */*
> Content-type: application/json
> Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ
> Content-Length: 13
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.3 Python/3.8.19
< Date: Thu, 20 Jun 2024 20:46:31 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 69
< Connection: close
< 
Запрос о просмотре успешно отправлен
* Closing connection 0
```

Пинг сервиса (всегда возвращает 200):

```
curl -v -X GET 'localhost:8092'
```
```
*   Trying 127.0.0.1:8092...
* Connected to localhost (127.0.0.1) port 8092 (#0)
> GET / HTTP/1.1
> Host: localhost:8092
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.3 Python/3.8.19
< Date: Thu, 20 Jun 2024 20:48:05 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 31
< Connection: close
< 
Hello from statistics service!
* Closing connection 0
```
