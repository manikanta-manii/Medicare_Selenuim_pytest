from base.db_connection import DatabaseAssessments


class DoctorsDB(DatabaseAssessments):

    def get_doctors_count(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM doctors")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_last_doctor_email(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(
            f"select email from users where(id = (select user_id from doctors ORDER BY id DESC LIMIT 1));")
        result = db_cursor.fetchone()[0]
        db.close()
        return result