from blueprints.cep import cep_blueprint


def setup_blueprints(app):
    app.register_blueprint(cep_blueprint)
