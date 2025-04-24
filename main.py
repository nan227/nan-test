from flask import Flask

app = Flask(__name__)

# Import routes
from routes import auth_routes, book_routes

app.register_blueprint(auth_routes)
app.register_blueprint(book_routes)

if __name__ == '__main__':
    app.run(debug=True)