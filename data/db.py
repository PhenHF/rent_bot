import sqlite3


def sql_con():
    con = sqlite3.connect('data/posts.db')
    return con


def select_post(user_id):
    con = sql_con()
    cur = con.cursor()

    user_info = cur.execute('SELECT posts FROM user_posts WHERE tg_user_id = ?', (user_id,)).fetchall()

    con.close()
    return user_info

def save_post(user_id, post):
    con = sql_con()
    cur = con.cursor()

    cur.execute('INSERT INTO user_posts(tg_user_id, posts) VALUES(?,?)',(user_id, post,) )

    con.commit()
    con.close()

def delete_post(user_id, post):
    con = sql_con()
    cur = con.cursor()

    cur.execute('DELETE FROM user_posts WHERE tg_user_id = ? and posts = ?',(user_id, post))

    con.commit()
    con.close()