import mysql.connector


class DatabaseAssessments:
    def __init__(self):
        pass

    def connect_to_db(self):
        medicare_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database='medicare_development_db'
        )
        return medicare_db
