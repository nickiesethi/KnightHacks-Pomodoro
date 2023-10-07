from flask import Flask
from endpoint import endpoint

app = Flask(__name__)
app.register_blueprint(endpoint, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
