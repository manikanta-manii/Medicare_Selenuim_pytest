from base.db_connection import DatabaseAssessments


class OrdersDB(DatabaseAssessments):

    def get_status(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT ordered FROM orders ORDER BY id DESC LIMIT 1")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_order_id(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT id FROM orders ORDER BY id DESC LIMIT 1")
        result = db_cursor.fetchone()[0]
        db.close()
        return result


