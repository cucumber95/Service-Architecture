from flask import Flask, request, make_response
import json
import hashlib
import jwt
import requests


def get_hash(cur_str):
    return hashlib.md5(cur_str.encode()).hexdigest()

def get_cookie(login, private):
    return jwt.encode({'login': login}, private, 'RS256')

def decode_cookie(kuka, public):
    return jwt.decode(kuka, public, ['RS256'])

def update_data(login, data):
    data['login'] = login
    response = requests.post('http://database:8091/data', data=json.dumps(data))
    return response.json()

def create_app(private, public) -> Flask:
    app = Flask(__name__)

    @app.route('/signup', methods=['POST'])
    def signup():
        body = json.loads(request.data)
        login = body['login']
        password = body['password']

        response = requests.get('http://database:8091/password', data=json.dumps({'login': login}))
        if response.status_code == 200:
            return make_response('Пользователь уже существует\n', 403)
        
        requests.post('http://database:8091/password', data=json.dumps({'login': login, 'password': get_hash(f'{login}{password}')}))
        requests.post('http://database:8091/data/init', data=json.dumps({'login': login}))
        return make_response('Успешная регистрация\n', 200, {'Set-Cookie': f'jwt={get_cookie(login, private)}'})

    @app.route('/login', methods=['POST'])
    def login():
        body = json.loads(request.data)
        login = body['login']
        password = body['password']

        response = requests.get('http://database:8091/password', data=json.dumps({'login': login}))
        if response.status_code == 403:
            return make_response('Пользователя с таким логином не существует\n', 401)
        
        cur_password = response.text
        
        if not cur_password == get_hash(f'{login}{password}'):
            return make_response('Неверный пароль к логину\n', 403)

        return make_response('Успешная авторизация\n', 200, {'Set-Cookie': f'jwt={get_cookie(login, private)}'})
    
    @app.route('/update', methods=['POST'])
    def update():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 401)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
            response = update_data(login, json.loads(request.data))
            return make_response(f'Успешное обновление данных пользователя\n{response}\n', 200)
        except:
            return make_response('Невалидная кука\n', 400)
            
    return app


def main():
    with open('auth/signature.pem', 'r') as f:
        private = f.read()
    with open('auth/signature.pub', 'r') as f:
        public = f.read()
    app = create_app(private, public)
    app.run(host='0.0.0.0', port=8090)

if __name__ == "__main__":
    main()

        




