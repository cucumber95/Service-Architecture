def create():
    return "CREATE TABLE tasks ( \
                id SERIAL PRIMARY KEY, \
                authorLogin TEXT, \
                title TEXT, \
                content TEXT, \
                status INT \
            )" 

def insert(authorLogin, title, content, status=None):
    if not status:
        status = 0
    return f"INSERT INTO tasks (authorLogin, title, content, status) VALUES ('{authorLogin}', '{title}', '{content}', {status}) RETURNING id"

def get_authorLogin(id):
    return f"SELECT authorLogin FROM tasks WHERE id={id}"

def update(id, title=None, content=None, status=None):
    if title:
        title = f"'{title}'"
    if content:
        content = f"'{content}'"

    s = str()
    for k, v in {"title": title, "content": content, "status": status}.items():
        if v:
            if len(s):
                s = s + ","
            s = s + f"{k}={v}"

    return f"UPDATE tasks \
             SET {s} \
             WHERE id={id}" 

def delete(id):
    return f"DELETE FROM tasks WHERE id={id}"

def select_task(id):
    return f"SELECT * FROM tasks WHERE id={id}"

def select_all_tasks(authorLogin):
    return f"SELECT * FROM tasks WHERE authorLogin='{authorLogin}'"

    

