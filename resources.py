from flask import jsonify
import sqlite3
from flask import abort



def list_users():

    conn = sqlite3.connect('app.db')

    print ("Opened database successfully");

    api_list = []

    cursor = conn.execute("SELECT username, full_name,    email, password, id from users")

    for row in cursor:
        a_dict = {}
        a_dict['username'] = row[0]
        a_dict['name'] = row[1]
        a_dict['email'] = row[2]
        a_dict['password'] = row[3]
        a_dict['id'] = row[4]
        api_list.append(a_dict)

    conn.close()

    return jsonify({'user_list': api_list})

def list_user(user_id):

    conn = sqlite3.connect('app.db')

    print ("Opened database successfully")

    api_list = []

    cursor = conn.cursor()

    cursor.execute("SELECT * from users where id=?", (user_id,))

    data = cursor.fetchall()

    if len(data) != 0:
        user = {}
        user['username'] = data[0][0]
        user['name'] = data[0][1]
        user['email'] = data[0][2]
        user['password'] = data[0][3]
        user['id'] = data[0][4]

    conn.close()

    return jsonify(user)


def home_index():
    conn = sqlite3.connect('app.db')
    print ("Opened database successfully");
    api_list=[]
    cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")

    for row in cursor:
        api = {}
        api['version'] = row[0]
        api['buildtime'] = row[1]
        api['methods'] = row[2]
        api['links'] = row[3]
        api_list.append(api)
    conn.close()

    return jsonify({'api_version': api_list}), 200


def add_user(new_user):
    conn = sqlite3.connect('app.db')

    print ("Opened database successfully")

    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? or email=?",(new_user['username'],new_user['email']))
    data = cursor.fetchall()

    if len(data) != 0:
        abort(409)
    else:
        cursor.execute("insert into users (username, email, password, full_name) values(?,?,?,?)",(new_user['username'],new_user['email'], new_user['password'], new_user['name']))
        conn.commit()

    conn.close()

    return "Success"

    #return jsonify(new_user)


def del_user(del_user):
    conn = sqlite3.connect('app.db')
    print ("Opened database successfully")

    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? ",(del_user,))
    data = cursor.fetchall()

    print ("Data", data)

    if len(data) == 0:
        abort(404)
    else:
        cursor.execute("delete from users where username==?",(del_user,))
        conn.commit()
        conn.close()
        return "Success"

def upd_user(user):

    conn = sqlite3.connect('app.db')
    print ("Opened database successfully");

    cursor=conn.cursor()
    cursor.execute("SELECT * from users where id=? ",(user['id'],))
    data = cursor.fetchall()

    print (data)

    if len(data) == 0:
        abort(404)
    else:
        key_list=user.keys()

        for i in key_list:
            if i != "id":
                print (user, i)
                cursor.execute("""UPDATE users SET {0} = ? WHERE id = ?""".format(i), (user[i], user['id']))
                conn.commit()

    return "Success"

def list_tweets():

    conn = sqlite3.connect('app.db')
    print ("Opened database successfully");

    api_list = []

    cursor=conn.cursor()
    cursor.execute("SELECT username, body, tweet_time, id from tweets")

    data = cursor.fetchall()
    print (data)
    print (len(data))

    if len(data) == 0:
        return api_list
    else:
        for row in data:
            tweets = {}

            tweets['tweetedby'] = row[0]
            tweets['body'] = row[1]
            tweets['timestamp'] = row[2]
            tweets['id'] = row[3]

            print (tweets)
            api_list.append(tweets)

    conn.close()

    print (api_list)
    return jsonify({'tweets_list': api_list})

def add_tweet(new_tweets):

    conn = sqlite3.connect('app.db')
    print ("Opened database successfully");

    cursor=conn.cursor()
    cursor.execute("SELECT * from users where username=? ",(new_tweets['username'],))
    data = cursor.fetchall()

    if len(data) == 0:
        abort(404)
    else:
        cursor.execute("INSERT into tweets (username, body, tweet_time) values(?,?,?)",(new_tweets['username'],new_tweets['body'], new_tweets['created_at']))
        conn.commit()
        return "Success"

def list_tweet(user_id):

    print (user_id)
    conn = sqlite3.connect('app.db')
    print ("Opened database successfully");

    cursor=conn.cursor()
    cursor.execute("SELECT * from tweets  where id=?",(user_id,))
    data = cursor.fetchall()

    print (data)

    if len(data) == 0:
        abort(404)
    else:

        user = {}
        user['id'] = data[0][0]
        user['username'] = data[0][1]
        user['body'] = data[0][2]
        user['tweet_time'] = data[0][3]

    conn.close()
    return jsonify(user)

