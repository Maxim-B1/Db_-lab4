from app.db import mysql

class IngredientsDAO:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT ingredient_id, name, description FROM Ingredients")
        rows = cur.fetchall()
        cur.close()
        return rows

    @staticmethod
    def get_by_id(ingredient_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT ingredient_id, name, description FROM Ingredients WHERE ingredient_id=%s", (ingredient_id,))
        row = cur.fetchone()
        cur.close()
        return row

    @staticmethod
    def create(name, description):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Ingredients (name, description) VALUES (%s,%s)", (name, description))
        mysql.connection.commit()
        last = cur.lastrowid
        cur.close()
        return last

    @staticmethod
    def update(ingredient_id, name, description):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Ingredients SET name=%s, description=%s WHERE ingredient_id=%s", (name, description, ingredient_id))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    @staticmethod
    def delete(ingredient_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Ingredients WHERE ingredient_id=%s", (ingredient_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    def get_with_ingredients(self):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT
                d.Id_drug, d.drug_name,
                i.ingredient_id, i.name AS ingredient_name,
                di.amount
            FROM Drugs_list d
            LEFT JOIN Drug_Ingredients di ON di.drug_id = d.Id_drug
            LEFT JOIN Ingredients i ON i.ingredient_id = di.ingredient_id
            ORDER BY d.Id_drug;
        """)

        rows = cur.fetchall()

        result = {}
        for drug_id, drug_name, ingr_id, ingr_name, amount in rows:
            if drug_id not in result:
                result[drug_id] = {
                    "drug_id": drug_id,
                    "drug_name": drug_name,
                    "ingredients": []
                }
            if ingr_id:
                result[drug_id]["ingredients"].append({
                    "id": ingr_id,
                    "name": ingr_name,
                    "amount": amount
                })

        return list(result.values())
