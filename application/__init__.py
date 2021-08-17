from flask import Flask

def create_app():
    app = Flask(__name__)
    from .admin.admin_routes import admin
    from .user.user_routes import user
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.config['SECRET_KEY'] = 'its my secret key'
    return app