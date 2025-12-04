from app.db import mysql

class SuppliersDAO:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT supplier_id, name, country, contact_info FROM Suppliers")
        rows = cur.fetchall()
        cur.close()
        return rows

    @staticmethod
    def get_by_id(supplier_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT supplier_id, name, country, contact_info FROM Suppliers WHERE supplier_id=%s", (supplier_id,))
        row = cur.fetchone()
        cur.close()
        return row

    @staticmethod
    def create(name, country, contact_info):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Suppliers (name, country, contact_info) VALUES (%s,%s,%s)", (name, country, contact_info))
        mysql.connection.commit()
        last = cur.lastrowid
        cur.close()
        return last

    @staticmethod
    def update(supplier_id, name, country, contact_info):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Suppliers SET name=%s, country=%s, contact_info=%s WHERE supplier_id=%s",
                    (name, country, contact_info, supplier_id))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    @staticmethod
    def delete(supplier_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Suppliers WHERE supplier_id=%s", (supplier_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows
