from flask import Blueprint, jsonify, request
from .controller import UsagesController

bp = Blueprint("usages", __name__, url_prefix="/usages")
ctrl = UsagesController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:usage_id>")
def get_by_id(usage_id):
    res = ctrl.get_by_id(usage_id)
    return (jsonify(res) if res else ("Not found", 404))

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:usage_id>")
def update(usage_id):
    updated = ctrl.update(usage_id, request.get_json())
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:usage_id>")
def delete(usage_id):
    deleted = ctrl.delete(usage_id)
    return jsonify({"deleted_rows": deleted})
