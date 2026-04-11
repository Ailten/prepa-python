import mysql.connetor
import json

class DBConnect():

    @classmethod
    def getAccessDB():

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

        access = DBConnect.getAccessDB()

        connection = None
        cursor = None

        try:

            connection = mysql.connector.connect(
                host='localhost',
                database='PrepaPySql',
                user=access.login,
                password=access.password
            )

            cursor = connection.execute(query)

            return cursor.fetchall()

        except Exception as e:
            raise e
        finally:
            if cursor != None and cursor:
                cursor.close()
            if connection != None and connection:
                connection.close()