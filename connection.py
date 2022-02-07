import  mysql.connector

def get_connection():
    #creating connection with db
    try:
        con = mysql.connector.connect(host='localhost',
                                      database='twitter_fetch', user='root', password='root', charset='utf8')

        return con


    except Exception as e:
        print("Error connecting to Database")

def save(cursor, id, tweet,author_id,created_at,lang):
    #inserting data into the db
    try:
        query = "INSERT INTO twitter_data (id, tweet,author_id,created_at,lang) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (id, tweet,author_id,created_at,lang))
        return True

    except Exception as e:
        pass