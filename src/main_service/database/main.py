from flask import Flask, request, make_response
import json
import interact


def create_app(connection) -> Flask:
    app = Flask(__name__)

    @app.route('/password', methods=['GET', 'POST'])
    def password():
        body = json.loads(request.data)
        login = body['login']
        if request.method == 'GET':
            password = interact.get_row(connection, "passwords", "login", f'"{login}"')
            if not password:
                return make_response('', 403)
            return make_response(password[0][1], 200)
        else:
            password = body['password']
            real_password = interact.get_row(connection, "passwords", "login", f'"{login}"')
            if real_password:
                return make_response('', 403)
            interact.insert_row(connection, "passwords", f'"{login}", "{password}"')
            return make_response('', 200)
        
    @app.route('/data', methods=['POST'])
    def data():
        body = json.loads(request.data)
        keys = ['firstName', 'lastName', 'birthDate', 'mail', 'phoneNumber']
        login = body['login']

        for key in keys:
            value = body.get(key, None)
            if value:
                interact.update_row(connection, "users_data", "login", f'"{login}"', key, f'"{value}"')

        row = interact.get_row(connection, "users_data", "login", f'"{login}"')
        resp_dict = dict()
        for i in range(len(keys)):
            if (row[0][i + 1]):
                resp_dict[keys[i]] = row[0][i + 1]

        return make_response(json.dumps(resp_dict), 200)
    
    @app.route('/data/init', methods=['POST'])
    def data_init():
        body = json.loads(request.data)
        login = body['login']

        interact.insert_empty_row(connection, "users_data", "login", f'"{login}"')
        return make_response('', 200)
    
    @app.route('/logins', methods=['GET'])
    def logins():
        logins = interact.get_logins(connection)
        logins_list = [l[0] for l in logins]
        return make_response(json.dumps(logins_list), 200)

    return app
    

def main():
    connection = interact.create_connection()
    interact.create_table(connection, "passwords", "login TEXT PRIMARY KEY, password TEXT")
    interact.create_table(connection, "users_data", "login TEXT PRIMARY KEY, firstName TEXT, lastName TEXT, birthDate DATE, mail TEXT, phoneNumber TEXT")

    app = create_app(connection)
    app.run(host='0.0.0.0', port=8091)

if __name__ == "__main__":
    main()