from flask import Blueprint, jsonify, request
from .controller import CategoriesController

bp = Blueprint("categories", __name__, url_prefix="/categories")
ctrl = CategoriesController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:category_id>")
def get_by_id(category_id):
    res = ctrl.get_by_id(category_id)
    return (jsonify(res) if res else ("Not found", 404))

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:category_id>")
def update(category_id):
    data = request.get_json()
    updated = ctrl.update(category_id, data)
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:category_id>")
def delete(category_id):
    deleted = ctrl.delete(category_id)
    return jsonify({"deleted_rows": deleted})

@bp.get("/with-drugs")
def get_categories_with_drugs():
    return jsonify(ctrl.get_categories_with_drugs())

