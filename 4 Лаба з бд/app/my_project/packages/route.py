from flask import Blueprint, jsonify, request
from .controller import PackagesController

bp = Blueprint("packages", __name__, url_prefix="/packages")
ctrl = PackagesController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:package_id>")
def get_by_id(package_id):
    res = ctrl.get_by_id(package_id)
    return (jsonify(res) if res else ("Not found", 404))

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:package_id>")
def update(package_id):
    updated = ctrl.update(package_id, request.get_json())
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:package_id>")
def delete(package_id):
    deleted = ctrl.delete(package_id)
    return jsonify({"deleted_rows": deleted})
