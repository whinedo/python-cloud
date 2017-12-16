from flask import jsonify
import sqlite3



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


