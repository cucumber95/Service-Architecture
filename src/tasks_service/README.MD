## Запуск

```
docker-compose build
docker-compose up
```

## Примеры

```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"title": "lol", "content": "kek"}' 'localhost:8090/tasks/create'
```

```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"taskId": 1, "title": "lol?", "content": "kek!", "status": "HIGH_PRIORITY"}' 'localhost:8090/tasks/update'
```

```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"taskId": 1}' 'localhost:8090/tasks/delete'
```

```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"taskId": 1}' 'localhost:8090/tasks/get'
```

```
curl -v -X POST -H 'Content-type: application/json' -H 'Cookie: jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6Im1ha3Nvbjk1cHJvIn0.GNW6kdUvIWVV414HEqL3G_GbOzAlWmf08pTla3BBZx7z51AJcIBiUWuFD_RjrrbvBnURReOSAF8IGhkxdMmEiCg9kj1J2Hfad_DCHQVwd5E4tWmcWXuySwkc6MXOZbxCLgCtjNx5HyWdyyXlzeL3RD8FuuPxRmktsEmR5ERr4Ei4OmNsVHcWlnjZubUyVPU0aHDcA_nSuF9DFbcEKgpMiwsteR4NTZq0hKn-xrzWFtdgsH-dEAhmIIxc1vw9dUc7N9PnC4dJRjkV0j7ilygnF44KcCK2umJuvxlyEz1nHYXa4vxZ9U82Ae1GQXU47TjXzWKXkAyZgoJ9ZD-dOedxYQ' -d '{"pageSize": 2, "page": 1}' 'localhost:8090/tasks/get_page'
```


