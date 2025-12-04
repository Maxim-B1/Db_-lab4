from flask import Blueprint, jsonify, request
from .controller import ManufacturersController

bp = Blueprint("manufacturers", __name__, url_prefix="/manufacturers")
ctrl = ManufacturersController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:manufacturer_id>")
def get_by_id(manufacturer_id):
    res = ctrl.get_by_id(manufacturer_id)
    return (jsonify(res) if res else ("Not found", 404))

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:manufacturer_id>")
def update(manufacturer_id):
    updated = ctrl.update(manufacturer_id, request.get_json())
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:manufacturer_id>")
def delete(manufacturer_id):
    deleted = ctrl.delete(manufacturer_id)
    return jsonify({"deleted_rows": deleted})
