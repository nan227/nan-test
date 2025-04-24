from flask import Flask
from routes import admin_routes, member_routes

app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin_routes)
app.register_blueprint(member_routes)

if __name__ == '__main__':
    app.run(debug=True)