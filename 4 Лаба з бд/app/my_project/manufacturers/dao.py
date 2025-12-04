from app.db import mysql

class ManufacturersDAO:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT manufacturer_id, name, country, contact_info FROM Manufacturers")
        rows = cur.fetchall()
        cur.close()
        return rows

    @staticmethod
    def get_by_id(manufacturer_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT manufacturer_id, name, country, contact_info FROM Manufacturers WHERE manufacturer_id=%s", (manufacturer_id,))
        row = cur.fetchone()
        cur.close()
        return row

    @staticmethod
    def create(name, country, contact_info):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Manufacturers (name, country, contact_info) VALUES (%s,%s,%s)", (name, country, contact_info))
        mysql.connection.commit()
        last = cur.lastrowid
        cur.close()
        return last

    @staticmethod
    def update(manufacturer_id, name, country, contact_info):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Manufacturers SET name=%s, country=%s, contact_info=%s WHERE manufacturer_id=%s",
                    (name, country, contact_info, manufacturer_id))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    @staticmethod
    def delete(manufacturer_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Manufacturers WHERE manufacturer_id=%s", (manufacturer_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows
