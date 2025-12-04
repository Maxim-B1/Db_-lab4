from app.db import mysql

class UsagesDAO:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT usage_id, description FROM Usages")
        rows = cur.fetchall()
        cur.close()
        return rows

    @staticmethod
    def get_by_id(usage_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT usage_id, description FROM Usages WHERE usage_id=%s", (usage_id,))
        row = cur.fetchone()
        cur.close()
        return row

    @staticmethod
    def create(description):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Usages (description) VALUES (%s)", (description,))
        mysql.connection.commit()
        last = cur.lastrowid
        cur.close()
        return last

    @staticmethod
    def update(usage_id, description):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Usages SET description=%s WHERE usage_id=%s", (description, usage_id))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    @staticmethod
    def delete(usage_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Usages WHERE usage_id=%s", (usage_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows
