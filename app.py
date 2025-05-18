import os
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
    port = int(os.environ.get("PORT", 5000))  # get PORT from env or default to 5000
    app.run(host="0.0.0.0", port=port)