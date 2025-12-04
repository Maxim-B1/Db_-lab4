from flask import Blueprint, jsonify, request
from .controller import IngredientsController

bp = Blueprint("ingredients", __name__, url_prefix="/ingredients")
ctrl = IngredientsController()

@bp.get("/")
def get_all():
    return jsonify(ctrl.get_all())

@bp.get("/<int:ingredient_id>")
def get_by_id(ingredient_id):
    res = ctrl.get_by_id(ingredient_id)
    return (jsonify(res) if res else ("Not found", 404))

@bp.post("/")
def create():
    data = request.get_json()
    new_id = ctrl.create(data)
    return jsonify({"created_id": new_id}), 201

@bp.put("/<int:ingredient_id>")
def update(ingredient_id):
    updated = ctrl.update(ingredient_id, request.get_json())
    return jsonify({"updated_rows": updated})

@bp.delete("/<int:ingredient_id>")
def delete(ingredient_id):
    deleted = ctrl.delete(ingredient_id)
    return jsonify({"deleted_rows": deleted})

@bp.get("/with-ingredients")
def get_with_ingredients():
    return jsonify(ctrl.get_with_ingredients())
