from flask import Flask
from app.utils.config_loader import load_config
from app.db import mysql

from app.my_project.categories.route import bp as categories_bp
from app.my_project.manufacturers.route import bp as manufacturers_bp
from app.my_project.drugs.route import bp as drugs_bp
from app.my_project.packages.route import bp as packages_bp
from app.my_project.ingredients.route import bp as ingredients_bp
from app.my_project.usages.route import bp as usages_bp
from app.my_project.suppliers.route import bp as suppliers_bp



def create_app():
    app = Flask(__name__)

    config = load_config("app/config/app.yml")
    app.config.update(config["mysql"])


    mysql.init_app(app)


    app.register_blueprint(categories_bp)
    app.register_blueprint(manufacturers_bp)
    app.register_blueprint(drugs_bp)
    app.register_blueprint(packages_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(usages_bp)
    app.register_blueprint(suppliers_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
