from base.db_connection import DatabaseAssessments


class MedicinesDB(DatabaseAssessments):
    def get_medicines_count(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT COUNT(*) FROM medicines")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_last_medicine_name(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT name from medicines ORDER BY id DESC LIMIT 1")
        result = db_cursor.fetchone()[0]
        db.close()
        return result
