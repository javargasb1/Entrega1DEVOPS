from flask import Flask, jsonify
from src.config import DATABASE_URL, PORT
from src.models import db
from src.resources.blacklist_post import bp as bp_post
from src.resources.blacklist_get import bp as bp_get

# Elastic Beanstalk busca este objeto:
application = Flask(__name__)

application.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(application)
with application.app_context():
    db.create_all()

@application.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

application.register_blueprint(bp_post)
application.register_blueprint(bp_get)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=PORT)
