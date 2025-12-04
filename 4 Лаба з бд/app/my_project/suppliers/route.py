from flask import Blueprint, jsonify, request
from .controller import SuppliersController

bp = Blueprint("suppliers", __name__, url_prefix="/suppliers")
ctrl = SuppliersController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:supplier_id>")
def get_by_id(supplier_id):
    res = ctrl.get_by_id(supplier_id)
    return (jsonify(res) if res else ("Not found", 404))

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:supplier_id>")
def update(supplier_id):
    updated = ctrl.update(supplier_id, request.get_json())
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:supplier_id>")
def delete(supplier_id):
    deleted = ctrl.delete(supplier_id)
    return jsonify({"deleted_rows": deleted})
