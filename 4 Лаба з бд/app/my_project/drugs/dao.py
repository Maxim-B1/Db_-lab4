from app.db import mysql

class DrugsDAO:
    def get_all(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT Id_drug, drug_name, category_id, manufacturer_id, description FROM Drugs_list")
        rows = cur.fetchall()
        cur.close()
        return rows

    def get_by_id(self, drug_id):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT Id_drug, drug_name, category_id, manufacturer_id, description FROM Drugs_list WHERE Id_drug=%s",
            (drug_id,)
        )
        row = cur.fetchone()
        cur.close()
        return row

    def create(self, data):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Drugs_list (drug_name, category_id, manufacturer_id, description) VALUES (%s,%s,%s,%s)",
            (data.get("drug_name"), data.get("category_id"), data.get("manufacturer_id"), data.get("description"))
        )
        mysql.connection.commit()
        last_id = cur.lastrowid
        cur.close()
        return last_id

    def update(self, drug_id, data):
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE Drugs_list 
               SET drug_name=%s, category_id=%s, manufacturer_id=%s, description=%s 
               WHERE Id_drug=%s""",
            (data.get("drug_name"), data.get("category_id"), data.get("manufacturer_id"),
             data.get("description"), drug_id)
        )
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    def delete(self, drug_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Drugs_list WHERE Id_drug=%s", (drug_id,))
        mysql.connection.commit()
        rows = cur.rowcount
        cur.close()
        return rows

    # 🔹 M:1 — виробник → його препарати
    def get_drugs_by_manufacturers(self):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT 
                m.manufacturer_id,
                m.name AS manufacturer_name,
                d.Id_drug,
                d.drug_name
            FROM Manufacturers m
            LEFT JOIN Drugs_list d ON d.manufacturer_id = m.manufacturer_id
            ORDER BY m.manufacturer_id;
        """)
        rows = cur.fetchall()
        cur.close()

        result = {}
        for row in rows:
            mid = row["manufacturer_id"]
            mname = row["manufacturer_name"]
            did = row["Id_drug"]
            dname = row["drug_name"]

            if mid not in result:
                result[mid] = {
                    "manufacturer_id": mid,
                    "manufacturer_name": mname,
                    "drugs": []
                }
            if did is not None:
                result[mid]["drugs"].append({
                    "drug_id": did,
                    "drug_name": dname
                })

        return list(result.values())

    # 🔹 M:M — препарат → інгредієнти
    def get_drugs_with_ingredients(self):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT
                d.Id_drug,
                d.drug_name,
                i.ingredient_id,
                i.name AS ingredient_name,
                di.amount
            FROM Drugs_list d
            LEFT JOIN Drug_Ingredients di ON di.drug_id = d.Id_drug
            LEFT JOIN Ingredients i ON i.ingredient_id = di.ingredient_id
            ORDER BY d.Id_drug;
        """)
        rows = cur.fetchall()
        cur.close()

        result = {}
        for row in rows:
            did = row["Id_drug"]
            dname = row["drug_name"]
            iid = row["ingredient_id"]
            iname = row["ingredient_name"]
            amount = row["amount"]

            if did not in result:
                result[did] = {
                    "drug_id": did,
                    "drug_name": dname,
                    "ingredients": []
                }

            if iid is not None:
                result[did]["ingredients"].append({
                    "ingredient_id": iid,
                    "name": iname,
                    "amount": amount
                })

        return list(result.values())

    # 🔹 M:M — препарат → usages
    def get_drugs_with_usages(self):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT
                d.Id_drug,
                d.drug_name,
                u.usage_id,
                u.description AS usage_description
            FROM Drugs_list d
            LEFT JOIN Drug_Usages du ON du.drug_id = d.Id_drug
            LEFT JOIN Usages u ON u.usage_id = du.usage_id
            ORDER BY d.Id_drug;
        """)
        rows = cur.fetchall()
        cur.close()

        result = {}
        for row in rows:
            did = row["Id_drug"]
            dname = row["drug_name"]
            uid = row["usage_id"]
            udesc = row["usage_description"]

            if did not in result:
                result[did] = {
                    "drug_id": did,
                    "drug_name": dname,
                    "usages": []
                }

            if uid is not None:
                result[did]["usages"].append({
                    "usage_id": uid,
                    "description": udesc
                })

        return list(result.values())
