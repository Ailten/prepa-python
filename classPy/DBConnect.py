import mysql.connector
import json

class DBConnect():

    @classmethod
    def getAccessDB(self):

        fileJson = None

        try:

            fileJson = open("password.json", "r")
            strJson = fileJson.read()
            return json.loads(strJson)

        except Exception as e:
            raise e
        finally:
            if fileJson != None and not fileJson.closed:
                fileJson.close()

    @classmethod
    def callToDB(self, query):

        connection = None
        cursor = None

        try:

            access = DBConnect.getAccessDB()  # get login, password for connect to DB.

            connection = mysql.connector.connect(  # establish a connection to DB.
                host='localhost',
                database='PrepaPySql',
                user=access['login'],
                password=access['password']
            )

            cursor = connection.cursor()
            cursor.execute(query)  # execute a query SQL.

            return cursor.fetchall()  # return the result of query.

        except Exception as e:
            raise e
        finally:
            if cursor != None and cursor:
                cursor.close()
            if connection != None and connection:
                connection.close()