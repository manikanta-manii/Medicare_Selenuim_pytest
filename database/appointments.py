from base.db_connection import DatabaseAssessments


class AppointmentsDB(DatabaseAssessments):

    def get_status(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT status FROM appointments ORDER BY id DESC LIMIT 1")
        result = db_cursor.fetchone()[0]
        db.close()
        return result