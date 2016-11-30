from flask import Flask

app = Flask(__name__)

from app.dogecoin import dogecoin
from app.bitcoin import bitcoin
from app.auth import auth

app.register_blueprint(bitcoin)
app.register_blueprint(dogecoin)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run("0.0.0.0", "9000")