from app.db import mysql

class PackagesDAO:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT package_id, type, quantity FROM Packages")
        rows = cur.fetchall()
        cur.close()
        return rows

    @staticmethod
    def get_by_id(package_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT package_id, type, quantity FROM Packages WHERE package_id=%s", (package_id,))
        row = cur.fetchone()
        cur.close()
        return row

    @staticmethod
    def create(type_, quantity):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Packages (type, quantity) VALUES (%s,%s)", (type_, quantity))
        mysql.connection.commit()
        last = cur.lastrowid
        cur.close()
        return last

    @staticmethod
    def update(package_id, type_, quantity):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Packages SET type=%s, quantity=%s WHERE package_id=%s", (type_, quantity, package_id))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    @staticmethod
    def delete(package_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Packages WHERE package_id=%s", (package_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows
