from flask import Blueprint, render_template, request



bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    


    return render_template("pages/home.html")