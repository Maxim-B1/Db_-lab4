from app.db import mysql

class CategoriesDAO:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT category_id, name, description FROM Categories")
        rows = cur.fetchall()
        cur.close()
        return rows

    @staticmethod
    def get_by_id(category_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT category_id, name, description FROM Categories WHERE category_id=%s", (category_id,))
        row = cur.fetchone()
        cur.close()
        return row

    @staticmethod
    def create(name, description):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Categories (name, description) VALUES (%s, %s)", (name, description))
        mysql.connection.commit()
        last = cur.lastrowid
        cur.close()
        return last

    @staticmethod
    def update(category_id, name, description):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Categories SET name=%s, description=%s WHERE category_id=%s", (name, description, category_id))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    @staticmethod
    def delete(category_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Categories WHERE category_id=%s", (category_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    def get_categories_with_drugs(self):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT 
                c.category_id, c.name AS category_name,
                d.Id_drug, d.drug_name
            FROM Categories c
            LEFT JOIN Drugs_list d ON d.category_id = c.category_id
            ORDER BY c.category_id;
        """)
        rows = cur.fetchall()

        result = {}
        for cat_id, cat_name, drug_id, drug_name in rows:
            if cat_id not in result:
                result[cat_id] = {
                    "category_id": cat_id,
                    "category_name": cat_name,
                    "drugs": []
                }
            if drug_id:
                result[cat_id]["drugs"].append({
                    "drug_id": drug_id,
                    "drug_name": drug_name
                })

        return list(result.values())

