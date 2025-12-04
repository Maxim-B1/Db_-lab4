from flask import Blueprint, jsonify, request
from .controller import DrugsController

bp = Blueprint("drugs", __name__, url_prefix="/drugs")
ctrl = DrugsController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:drug_id>")
def get_by_id(drug_id):
    res = ctrl.get_by_id(drug_id)
    return jsonify(res) if res else ("Not found", 404)

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:drug_id>")
def update(drug_id):
    data = request.get_json()
    updated = ctrl.update(drug_id, data)
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:drug_id>")
def delete(drug_id):
    deleted = ctrl.delete(drug_id)
    return jsonify({"deleted_rows": deleted})

# 🔹 M:1 – всі виробники + їхні препарати
@bp.get("/manufacturers")
def drugs_by_manufacturers():
    return jsonify(ctrl.get_drugs_by_manufacturers())

# 🔹 M:M – препарати з інгредієнтами
@bp.get("/with-ingredients")
def drugs_with_ingredients():
    return jsonify(ctrl.get_drugs_with_ingredients())

# 🔹 M:M – препарати з usages
@bp.get("/with-usages")
def drugs_with_usages():
    return jsonify(ctrl.get_drugs_with_usages())
