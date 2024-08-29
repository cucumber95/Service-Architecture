## Запуск

```
docker-compose build
docker-compose up
```

## Описание

Сервис написан на python с использованием библиотеки flask. В соседнем контейнере поднимается SQLite база данных с двумя таблицами: в одной хранятся пароли пользователей (точнее хеши), в другой - информация о них. Внутри сервера хранятся сгенерированные RSA ключи, с помощью которых генерируются и возвращаются клиенту JWT-токены (возвращаются в хедере 'Set-Cookie' на успешный /login или /signup запрос) - с помощью данной куки клиент будет в дальнейшем обращаться к серверу (передавая хедером в методе /update).

## Примеры

```
curl -v -X POST -H 'Content-type: application/json' -d '{"login": "makson95pro", "password": "123"}' 'localhost:8090/signup'
```
```
*   Trying 127.0.0.1:8090...
* Connected to localhost (127.0.0.1) port 8090 (#0)
> POST /signup HTTP/1.1
> Host: localhost:8090
> User-Agent: curl/7.81.0
> Accept: */*
> Content-type: application/json
> Content-Length: 43
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.8.19
< Date: Mon, 01 Apr 2024 17:13:00 GMT
< Set-Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ
< Content-Type: text/html; charset=utf-8
< Content-Length: 40
< Connection: close
< 
Успешная регистрация
```
```
curl -v -X POST -H 'Content-type: application/json' -d '{"login": "makson95pro", "password": "123"}' 'localhost:8090/login'
```
```
*   Trying 127.0.0.1:8090...
* Connected to localhost (127.0.0.1) port 8090 (#0)
> POST /login HTTP/1.1
> Host: localhost:8090
> User-Agent: curl/7.81.0
> Accept: */*
> Content-type: application/json
> Content-Length: 43
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.8.19
< Date: Mon, 01 Apr 2024 17:14:25 GMT
< Set-Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ
< Content-Type: text/html; charset=utf-8
< Content-Length: 40
< Connection: close
< 
Успешная авторизация
```
```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"firstName": "Maksim", "lastName": "Galkin", "birthDate": "15.09.2003", "mail": "maksgal15.09@gmail.com", "phoneNumber": "+79960032654"}' 'localhost:8090/update'
```
```
*   Trying 127.0.0.1:8090...
* Connected to localhost (127.0.0.1) port 8090 (#0)
> POST /update HTTP/1.1
> Host: localhost:8090
> User-Agent: curl/7.81.0
> Accept: */*
> Content-type: application/json
> Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ
> Content-Length: 137
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.8.19
< Date: Mon, 01 Apr 2024 17:21:16 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 214
< Connection: close
< 
Успешное обновление данных пользователя
{'firstName': 'Maksim', 'lastName': 'Galkin', 'birthDate': '15.09.2003', 'mail': 'maksgal15.09@gmail.com', 'phoneNumber': '+79960032654'}
```



