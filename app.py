from flask import Flask
from routes.estimation import estimation_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enables CORS for all routes

app.register_blueprint(estimation_bp)

@app.route('/')
def home():
    return "API Flask funcionando!"

if __name__ == '__main__':
    app.run(debug=True)
