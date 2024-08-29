def drop_likes_table():
    return "DROP TABLE IF EXISTS likes_stats"

def drop_views_table():
    return "DROP TABLE IF EXISTS views_stats"

def create_likes_table():
    return "CREATE TABLE IF NOT EXISTS likes_stats ( \
        taskId UInt64, \
        login String, \
        timestamp DateTime \
        ) engine = MergeTree() \
        ORDER BY taskId \
        PRIMARY KEY taskId"

def create_views_table():
    return "CREATE TABLE IF NOT EXISTS views_stats ( \
        taskId UInt64, \
        login String, \
        timestamp DateTime \
        ) engine = MergeTree() \
        ORDER BY taskId \
        PRIMARY KEY taskId"

def get_likes():
    return f"SELECT * FROM likes_stats"

def get_views():
    return f"SELECT * FROM views_stats"

def insert_like(taskId, login):
    return f"INSERT INTO likes_stats (taskId, login, timestamp) VALUES ({taskId}, '{login}', now())"

def insert_view(taskId, login):
    return f"INSERT INTO views_stats (taskId, login, timestamp) VALUES ({taskId}, '{login}', now())"